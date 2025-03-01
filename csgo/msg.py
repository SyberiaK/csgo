"""Various utility function for dealing with messages."""
from __future__ import annotations


from google.protobuf.reflection import GeneratedProtocolMessageType

from csgo.enums import EGCBaseClientMsg, ECsgoGCMsg, EGCItemMsg
from csgo.protobufs import (gcsdk_gcmessages_pb2, cstrike15_gcmessages_pb2,
                            econ_gcmessages_pb2, base_gcmessages_pb2)


def get_emsg_enum(emsg):
    """
    Attempts to find the Enum for the given :class:`int`

    :param emsg: integer corresponding to a Enum
    :type emsg: :class:`int`
    :return: Enum if found, `emsg` if not
    :rtype: Enum, :class:`int`
    """
    for enum in EGCBaseClientMsg, ECsgoGCMsg, EGCItemMsg:
        try:
            return enum(emsg)
        except ValueError:
            pass

    return emsg


def find_proto(emsg) -> GeneratedProtocolMessageType | None:
    """
    Attempts to find the protobuf message for a given Enum

    :param emsg: Enum corrensponding to a protobuf message
    :type emsg: `Enum`
    :return: protobuf message class
    """

    if type(emsg) is int:
        return

    if proto := _proto_map_why_cant_we_name_things_properly.get(emsg):
        return proto

    for module in (gcsdk_gcmessages_pb2, cstrike15_gcmessages_pb2,
                   econ_gcmessages_pb2, base_gcmessages_pb2):
        proto = getattr(module, emsg.name.replace("EMsg", "CMsg"), None)

        if proto is None:
            proto = getattr(module, emsg.name.replace("EMsgGC", "CMsg"), None)

        if proto:
            return proto

    return proto  # should always be `None`


_proto_map_why_cant_we_name_things_properly = {
    EGCBaseClientMsg.EMsgGCClientConnectionStatus: gcsdk_gcmessages_pb2.CMsgConnectionStatus,
    EGCBaseClientMsg.EMsgGCClientHelloPartner: gcsdk_gcmessages_pb2.CMsgClientHello,
    EGCBaseClientMsg.EMsgGCClientHelloPW: gcsdk_gcmessages_pb2.CMsgClientHello,
    EGCBaseClientMsg.EMsgGCClientHelloR2: gcsdk_gcmessages_pb2.CMsgClientHello,
    EGCBaseClientMsg.EMsgGCClientHelloR3: gcsdk_gcmessages_pb2.CMsgClientHello,
    EGCBaseClientMsg.EMsgGCClientHelloR4: gcsdk_gcmessages_pb2.CMsgClientHello,
    ECsgoGCMsg.EMsgGCCStrike15_v2_ClientRequestWatchInfoFriends2: cstrike15_gcmessages_pb2.CMsgGCCStrike15_v2_ClientRequestWatchInfoFriends,
    ECsgoGCMsg.EMsgGCCStrike15_v2_GC2ClientGlobalStats: cstrike15_gcmessages_pb2.GlobalStatistics,
}
