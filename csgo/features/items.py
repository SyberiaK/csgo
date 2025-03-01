from __future__ import annotations

from typing import TYPE_CHECKING

from csgo.enums import ECsgoGCMsg

if TYPE_CHECKING:
    from csgo.client import CSGOClient


class Items:
    def __init__(self: CSGOClient):
        # register our handlers
        self.on(ECsgoGCMsg.EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse, self.__handle_preview_data_block)

    def request_preview_data_block(self: CSGOClient, s: int, a: int, d: int, m: int):
        """
        Request item preview data block

        The parameters can be taken from ``inspect`` links either from an inventory or market.
        The market has the ``m`` paramter, while the inventory one has ``s``.
        Set the missing one to ``0``. Example ``inpsect`` links:

        .. code:: text

            steam://rungame/730/765xxxxxxxxxxxxxx/+csgo_econ_action_preview%20S11111111111111111A2222222222D33333333333333333333``
            steam://rungame/730/765xxxxxxxxxxxxxx/+csgo_econ_action_preview%20M444444444444444444A2222222222D33333333333333333333``

        :param s: steam id of owner (set to ``0`` if not available)
        :type s: :class:`int`
        :param a: item id
        :type a: :class:`int`
        :param d: UNKNOWN
        :type d: :class:`int`
        :param m: market id (set to ``0`` if not available)
        :type m: :class:`int`

        Response event: ``item_data_block``

        :param message: `CEconItemPreviewDataBlock <https://github.com/ValvePython/csgo/blob/386b76b17640f7717fe9ead5a6a607e0c821010c/protobufs/cstrike15_gcmessages.proto#L681>`_
        :type message: proto message

        """
        self.send(ECsgoGCMsg.EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockRequest, {'param_s': s,
                                                                                       'param_a': a,
                                                                                       'param_d': d,
                                                                                       'param_m': m, })

    def __handle_preview_data_block(self: CSGOClient, message):
        self.emit("item_data_block", message.iteminfo)
