"""Essentially a :class:`dict` containing shared object caches.
The objects are read-only, so don't change any values.
The instance reference of individual objects will remain the same thought their lifetime.
Individual objects can be accessed via their key, if they have one.

.. note::
    Some cache types don't have a key and only hold one object instance.
    Then only the the cache type is needed to access it.
    (e.g. ``CSOEconGameAccountClient``)

.. code:: python

    csgo_client.socache[ESOType.CSOEconItem]          # dict with item objects, key = item id
    csgo_client.socache[ESOType.CSOEconItem][123456]  # item object

    csgo_client.socache[ESOType.CSOEconGameAccountClient]  # returns a CSOEconGameAccountClient object

Events will be fired when individual objects are updated.
Event key is a :class:`tuple`` in the following format: ``(event, cache_type)``.

The available events are ``new``, ``updated``, and ``removed``.
Each event has a single parameter, which is the object instance.
Even when removed, there is object instance returned, usually only with the key field filled.

.. code:: python

    @csgo_client.socache.on(('new', ESOType.CSOEconItem))
    def got_a_new_item(obj):
        print "Got a new item! Yay"
        print obj

    # access the item via socache at any time
    print csgo_client.socache[ESOType.CSOEconItem][obj.id]

"""
import logging
from eventemitter import EventEmitter

from csgo.enums import EGCBaseClientMsg, ESOMsg, ESOType
from csgo.protobufs import base_gcmessages_pb2 as _gc_base
from csgo.protobufs import cstrike15_gcmessages_pb2 as _gc_cstrike


def find_so_proto(type_id):
    """
    Resolves proto massage for given type_id

    :param type_id: SO type
    :type type_id: :class:`csgo.enums.ESOType`
    :returns: proto message or `None`
    """

    if not isinstance(type_id, ESOType):
        return None

    proto = getattr(_gc_base, type_id.name, None)
    if proto is None:
        proto = getattr(_gc_cstrike, type_id.name, None)

    return proto


# a sentinel to mark certain CSO as having no key
NO_KEY = object()

so_key_fields = {
    # _gc_base.CSOPartyInvite.DESCRIPTOR: ['group_id'],
    # _gc_base.CSOLobbyInvite.DESCRIPTOR: ['group_id'],
    # _gc_base.CSOEconItemLeagueViewPass.DESCRIPTOR: ['account_id', 'league_id'],
    # _gc_base.CSOEconDefaultEquippedDefinitionInstanceClient.DESCRIPTOR: ['account_id', 'class_id', 'slot_id'],
    _gc_base.CSOEconItem.DESCRIPTOR: ['id'],
    _gc_base.CSOEconGameAccountClient.DESCRIPTOR: NO_KEY,
    _gc_base.CSOEconItemEventTicket.DESCRIPTOR: NO_KEY,
    _gc_cstrike.CSOPersonaDataPublic.DESCRIPTOR: NO_KEY,
    # _gc_cstrike.CSOEconCoupon.DESCRIPTOR: ['entryid'],
    # _gc_cstrike.CSOQuestProgress.DESCRIPTOR: ['questid'],
}


# key is either one or a number of fields marked with option 'key_field'=true in protos
def get_so_key_fields(desc):
    if desc in so_key_fields:
        return so_key_fields[desc]

    fields = []

    for field in desc.fields:
        for odesc, value in field.GetOptions().ListFields():
            if odesc.name == 'key_field' and value is True:
                fields.append(field.name)

    so_key_fields[desc] = fields
    return fields


def get_key_for_object(obj):
    key = get_so_key_fields(obj.DESCRIPTOR)

    if key is NO_KEY:
        return NO_KEY
    if not key:
        return None
    if len(key) == 1:
        return getattr(obj, key[0])

    return tuple(map(lambda x: getattr(obj, x), key))


class SOBase:
    def __init__(self):
        #: Shared Object Caches
        name = f"{self.__class__.__name__}.socache"
        self.socache = SOCache(self, name)


class SOCache(EventEmitter, dict):
    ESOType = ESOType  #: expose ESOType

    def __init__(self, csgo_client, logger_name):
        from csgo.client import CSGOClient

        super().__init__()

        self._LOG = logging.getLogger(logger_name if logger_name else self.__class__.__name__)
        self._caches = {}
        self._csgo = csgo_client

        # register our handlers
        csgo_client.on(ESOMsg.Create, self._handle_create)
        csgo_client.on(ESOMsg.Update, self._handle_update)
        csgo_client.on(ESOMsg.Destroy, self._handle_destroy)
        csgo_client.on(ESOMsg.UpdateMultiple, self._handle_update_multiple)
        csgo_client.on(ESOMsg.CacheSubscribed, self._handle_cache_subscribed)
        csgo_client.on(ESOMsg.CacheUnsubscribed, self._handle_cache_unsubscribed)
        csgo_client.on(EGCBaseClientMsg.EMsgGCClientWelcome, self._handle_client_welcome)
        csgo_client.on(CSGOClient.EVENT_READY, self._handle_cleanup)

    def __hash__(self):
        # pretend that we are a hashable dict, lol
        # don't attach more than one SOCache per CSGOClient
        return hash((self._csgo, 42))

    def __getitem__(self, key):
        try:
            key = ESOType(key)
        except ValueError:
            raise KeyError(str(key))

        if key not in self:
            self[key] = {}
        return dict.__getitem__(self, key)

    def __repr__(self):
        return f'<SOCache({self._csgo!r})>'

    def emit(self, event, *args):
        if event is not None:
            self._LOG.debug(f'Emit event: {event!r}')
        super(SOCache, self).emit(event, *args)

    def _handle_cleanup(self):
        for v in self.values():
            if isinstance(v, dict):
                v.clear()
        self.clear()
        self._caches.clear()

    def _get_proto_for_type(self, type_id):
        try:
            type_id = ESOType(type_id)
        except ValueError:
            self._LOG.error(f"Unsupported type: {type_id}")
            return

        proto = find_so_proto(type_id)

        if proto is None:
            self._LOG.error(f"Unable to locate proto for: {type_id!r}")
            return

        return proto

    def _parse_object_data(self, type_id, object_data):
        proto = self._get_proto_for_type(type_id)

        if proto is None:
            return

        if not get_so_key_fields(proto.DESCRIPTOR):
            self._LOG.error(f"Unable to find key for {type_id}")
            return

        obj = proto.FromString(object_data)
        key = get_key_for_object(obj)

        return key, obj

    def _update_object(self, type_id, object_data):
        result = self._parse_object_data(type_id, object_data)
        if not result:
            return

        key, obj = result
        type_id = ESOType(type_id)

        if key is NO_KEY:
            if not isinstance(self[type_id], dict):
                self[type_id].CopyFrom(obj)
                obj = self[type_id]
            else:
                self[type_id] = obj
        else:
            if key in self[type_id]:
                self[type_id][key].CopyFrom(obj)
                obj = self[type_id][key]
            else:
                self[type_id][key] = obj

        return type_id, obj

    def _handle_create(self, message):
        result = self._update_object(message.type_id, message.object_data)
        if not result:
            return

        type_id, obj = result
        self.emit(('new', type_id), obj)

    def _handle_update(self, message):
        result = self._update_object(message.type_id, message.object_data)
        if not result:
            return

        type_id, obj = result
        self.emit(('updated', type_id), obj)

    def _handle_destroy(self, message):
        result = self._parse_object_data(message.type_id, message.object_data)
        if not result:
            return
        key, obj = result
        type_id = ESOType(message.type_id)

        if key is NO_KEY:
            current = self.pop(type_id, None)
        else:
            current = self[type_id].pop(key, None)

        if current:
            current.CopyFrom(obj)

        self.emit(('removed', type_id), current or obj)

    def _handle_update_multiple(self, message):
        for so_object in message.objects_modified:
            self._handle_update(so_object)

    #       for so_object in message.objects_added:
    #           self._handle_create(so_object)
    #       for so_object in message.objects_removed:
    #           self._handle_destroy(so_object)

    def _handle_client_welcome(self, message):
        for one in message.outofdate_subscribed_caches:
            self._handle_cache_subscribed(one)

    def _handle_cache_subscribed(self, message):
        cache_key = message.owner_soid.type, message.owner_soid.id
        self._caches.setdefault(cache_key, dict())

        cache = self._caches[cache_key]
        cache['version'] = message.version
        cache.setdefault('type_ids', set()).update(map(lambda x: x.type_id, message.objects))

        for objects in message.objects:
            for object_bytes in objects.object_data:
                result = self._update_object(objects.type_id, object_bytes)
                if not result:
                    break

                type_id, obj = result
                self.emit(('new', type_id), obj)

    def _handle_cache_unsubscribed(self, message):
        cache_key = message.owner_soid.type, message.owner_soid.id

        if cache_key not in self._caches:
            return
        cache = self._caches[cache_key]

        for type_id in cache['type_ids']:
            if type_id not in self:
                continue

            type_id = ESOType(type_id)

            field = self[type_id]

            if isinstance(field, dict):
                for key in list(field.keys()):
                    self.emit(('removed', type_id), self[type_id].pop(key))
            else:
                self.emit(('removed', type_id), self.pop(type_id))

            del self[type_id]
        del self._caches[cache_key]
