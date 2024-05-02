"""
Only the most essential features to :class:`csgo.client.CSGOClient` are found here. Every other feature is inherited from
the :mod:`csgo.features` package and it's submodules.
"""

import logging
import gevent
import google.protobuf
from steam.core.msg import GCMsgHdrProto
from steam.client.gc import GameCoordinator
from steam.enums.emsg import EMsg
from steam.utils.proto import proto_fill_from_dict
from csgo.features import FeatureBase
from csgo.enums import EGCBaseClientMsg, GCConnectionStatus, GCClientLauncherType
from csgo.msg import get_emsg_enum, find_proto
from csgo.protobufs import gcsdk_gcmessages_pb2 as pb_gc
from csgo.protobufs import cstrike15_gcmessages_pb2 as pb_gclient


class CSGOClient(GameCoordinator, FeatureBase):
    """
    :param steam_client: Instance of the steam client
    :type steam_client: :class:`steam.client.SteamClient`
    """
    _retry_welcome_loop = None
    verbose_debug = False
    #: enable pretty print of messages in debug logging
    app_id = 730
    #: main client app id
    launcher = GCClientLauncherType.DEFAULT
    #: launcher type (used for access to PW) See: :class:`csgo.enums.GCClientLauncherType`
    current_jobid = 0
    ready = False
    #: ``True`` when we have a session with GC
    connection_status = GCConnectionStatus.NO_SESSION
    #: See :class:`csgo.enums.GCConnectionStatus`

    @property
    def account_id(self):
        """
        Account ID of the logged-in user in the steam client
        """
        return self.steam.steam_id.id

    @property
    def steam_id(self):
        """
        :class:`steam.steamid.SteamID` of the logged-in user in the steam client
        """
        return self.steam.steam_id

    def __init__(self, steam_client):
        GameCoordinator.__init__(self, steam_client, self.app_id)
        self._LOG = logging.getLogger(self.__class__.__name__)

        FeatureBase.__init__(self)

        self.steam.on('disconnected', self._handle_disconnect)
        self.steam.on(EMsg.ClientPlayingSessionState, self._handle_play_sess_state)

        # register GC message handles
        self.on(EGCBaseClientMsg.EMsgGCClientConnectionStatus, self._handle_conn_status)
        self.on(EGCBaseClientMsg.EMsgGCClientWelcome, self._handle_client_welcome)

    def __repr__(self):
        return "<%s(%s) %s>" % (self.__class__.__name__,
                                              repr(self.steam),
                                              repr(self.connection_status),
                                              )

    def _handle_play_sess_state(self, message):
        if self.ready and message.playing_app != self.app_id:
            self._set_connection_status(GCConnectionStatus.NO_SESSION)

    def _handle_disconnect(self):
        if self._retry_welcome_loop:
            self._retry_welcome_loop.kill()

        self._set_connection_status(GCConnectionStatus.NO_SESSION)

    def _handle_client_welcome(self, message):
        self._set_connection_status(GCConnectionStatus.HAVE_SESSION)

        # handle CSGO Welcome
        submessage = pb_gclient.CMsgCStrike15Welcome()
        submessage.ParseFromString(message.game_data)

        if self.verbose_debug:
            self._LOG.debug("Got CStrike15Welcome:\n%s" % str(submessage))
        else:
            self._LOG.debug("Got CStrike15Welcome")

        self.emit('csgo_welcome', submessage)

    def _handle_conn_status(self, message):
        self._set_connection_status(message.status)

    def _process_gc_message(self, emsg, header, payload):
        emsg = get_emsg_enum(emsg)
        proto = find_proto(emsg)

        if proto is None:
            self._LOG.error("Failed to parse: %s" % repr(emsg))
            return

        message = proto()
        message.ParseFromString(payload)

        if self.verbose_debug:
            self._LOG.debug("Incoming: %s\n%s\n---------\n%s" % (repr(emsg),
                                                              str(header),
                                                              str(message),
                                                              ))
        else:
            self._LOG.debug("Incoming: %s", repr(emsg))

        self.emit(emsg, message)

        if header.proto.job_id_target != 18446744073709551615:
            self.emit('job_%d' % header.proto.job_id_target, message)

    def _set_connection_status(self, status):
        prev_status = self.connection_status
        self.connection_status = GCConnectionStatus(status)

        if self.connection_status != prev_status:
            self.emit("connection_status", self.connection_status)

        if self.connection_status == GCConnectionStatus.HAVE_SESSION and not self.ready:
            self.ready = True
            self.emit('ready')
        elif self.connection_status != GCConnectionStatus.HAVE_SESSION and self.ready:
            self.ready = False
            self.emit('notready')

    def wait_msg(self, event, timeout=None, raises=None):
        """Wait for a message, similiar to :meth:`.wait_event`

        :param event: event id
        :type  event: :class:`.ECsgoGCMsg` or job id
        :param timeout: seconds to wait before timeout
        :type  timeout: :class:`int`
        :param raises: On timeout when ``False`` returns :class:`None`, else raise :class:`gevent.Timeout`
        :type  raises: :class:`bool`
        :return: returns a message or :class:`None`
        :rtype: :class:`None`, or `proto message`
        :raises: :class:`gevent.Timeout`
        """
        resp = self.wait_event(event, timeout, raises)

        if resp is not None:
            return resp[0]

    def send_job(self, *args, **kwargs):
        """
        Send a message as a job

        Exactly the same as :meth:`send`

        :return: jobid event identifier
        :rtype: :class:`str`

        """
        jobid = self.current_jobid = ((self.current_jobid + 1) % 10000) or 1
        self.remove_all_listeners('job_%d' % jobid)

        self._send(*args, jobid=jobid, **kwargs)

        return "job_%d" % jobid

    def send(self, emsg, data={}, proto=None):
        """
        Send a message

        :param emsg: Enum for the message
        :param data: data for the proto message
        :type data: :class:`dict`
        :param proto: (optional) manually specify protobuf, other it's detected based on ``emsg``
        """
        self._send(emsg, data, proto)

    def _send(self, emsg, data={}, proto=None, jobid=None):
        if not isinstance(data, dict):
            raise ValueError("data kwarg can only be a dict")

        if proto is None:
            proto = find_proto(emsg)

        if proto is None or not issubclass(proto, google.protobuf.message.Message):
            raise ValueError("Unable to find proto for emsg, or proto kwarg is invalid")

        message = proto()
        proto_fill_from_dict(message, data)

        header = GCMsgHdrProto(emsg)

        if jobid is not None:
            header.proto.job_id_source = jobid

        if self.verbose_debug:
            str_message = ''
            str_header = str(header)
            str_body = str(message)

            if str_header:
                str_message += "-- header ---------\n%s\n" % str_header
            if str_body:
                str_message += "-- message --------\n%s\n" % str_body

            self._LOG.debug("Outgoing: %s\n%s" % (repr(emsg), str_message))
        else:
            self._LOG.debug("Outgoing: %s", repr(emsg))

        GameCoordinator.send(self, header, message.SerializeToString())

    def _knock_on_gc(self):
            n = 1

            while True:
                if not self.ready:
                    if self.launcher == GCClientLauncherType.PERFECTWORLD:
                        self.send(EGCBaseClientMsg.EMsgGCClientHelloPW, {
                            'client_launcher': self.launcher,
                            })
                    else:  # GCClientLauncherType.DEFAULT
                        self.send(
                            EGCBaseClientMsg.EMsgGCClientHello,
                            {
                                'version': 2000202
                            },
                        )

                    self.wait_event('ready', timeout=3 + (2**n))
                    n = min(n + 1, 4)

                else:
                    self.wait_event('notready')
                    n = 1
                    gevent.sleep(1)

    def launch(self):
        """
        Launch CSGO and establish connection with the game coordinator

        ``ready`` event will fire when the session is ready.
        If the session is lost ``notready`` event will fire.
        Alternatively, ``connection_status`` event can be monitored for changes.
        """
        if not self.steam.logged_on:
            self.steam.wait_event('logged_on')

        if not self._retry_welcome_loop and self.app_id not in self.steam.current_games_played:
            self.steam.games_played(self.steam.current_games_played + [self.app_id])
            self._retry_welcome_loop = gevent.spawn(self._knock_on_gc)

    def exit(self):
        """
        Close connection to CSGO's game coordinator
        """
        if self._retry_welcome_loop:
            self._retry_welcome_loop.kill()

        if self.app_id in self.steam.current_games_played:
            self.steam.current_games_played.remove(self.app_id)
            self.steam.games_played(self.steam.current_games_played)

        self._set_connection_status(GCConnectionStatus.NO_SESSION)
