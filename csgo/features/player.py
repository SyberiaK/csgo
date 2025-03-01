from __future__ import annotations

from typing import TYPE_CHECKING

from csgo.enums import ECsgoGCMsg

if TYPE_CHECKING:
    from csgo.client import CSGOClient


class Player:
    ranks_map = {
        0: "Not Ranked",
        1: "Silver I",
        2: "Silver II",
        3: "Silver III",
        4: "Silver IV",
        5: "Silver Elite",
        6: "Silver Elite Master",
        7: "Gold Nova I",
        8: "Gold Nova II",
        9: "Gold Nova III",
        10: "Gold Nova Master",
        11: "Master Guardian I",
        12: "Master Guardian II",
        13: "Master Guardian Elite",
        14: "Distinguished Master Guardian",
        15: "Legendary Eagle",
        16: "Legendary Eagle Master",
        17: "Supreme Master First Class",
        18: "The Global Elite"
    }
    """:class:`dict` mapping rank id to name"""
    wingman_ranks_map = ranks_map
    """:class:`dict` mapping wingman rank id to name"""
    dangerzone_ranks_map = {
        0: "Hidden",
        1: "Lab Rat I",
        2: "Lab Rat II",
        3: "Sprinting Hare I",
        4: "Sprinting Hare II",
        5: "Wild Scout I",
        6: "Wild Scout II",
        7: "Wild Scout Elite",
        8: "Hunter Fox I",
        9: "Hunter Fox II",
        10: "Hunter Fox II",
        11: "Hunter Fox Elite",
        12: "Timber Wolf",
        13: "Ember Wolf",
        14: "Wildfire Wolf",
        15: "The Howling Alpha"
    }
    """:class:`dict` mapping dangerzone rank id to name"""
    levels_map = {
        0: 'Not Recruited',
        1: 'Recruit',
        2: 'Private',
        3: 'Private',
        4: 'Private',
        5: 'Corporal',
        6: 'Corporal',
        7: 'Corporal',
        8: 'Corporal',
        9: 'Sergeant',
        10: 'Sergeant',
        11: 'Sergeant',
        12: 'Sergeant',
        13: 'Master Sergeant',
        14: 'Master Sergeant',
        15: 'Master Sergeant',
        16: 'Master Sergeant',
        17: 'Sergeant Major',
        18: 'Sergeant Major',
        19: 'Sergeant Major',
        20: 'Sergeant Major',
        21: 'Lieutenant',
        22: 'Lieutenant',
        23: 'Lieutenant',
        24: 'Lieutenant',
        25: 'Captain',
        26: 'Captain',
        27: 'Captain',
        28: 'Captain',
        29: 'Major',
        30: 'Major',
        31: 'Major',
        32: 'Major',
        33: 'Colonel',
        34: 'Colonel',
        35: 'Colonel',
        36: 'Brigadier General',
        37: 'Major General',
        38: 'Lieutenant General',
        39: 'General',
        40: 'Global General'
    }
    """:class:`dict` mapping level to name"""

    def __init__(self: CSGOClient):
        # register our handlers
        self.on(ECsgoGCMsg.EMsgGCCStrike15_v2_PlayersProfile, self.__handle_player_profile)

    def request_player_profile(self: CSGOClient, account_id, request_level: int = 32):
        """
        Request player profile

        :param account_id: account id
        :type account_id: :class:`int`
        :param request_level: no clue what this is used for; if you do, please make pull request
        :type request_level: :class:`int`

        Response event: ``player_profile``

        :param message: `CMsgGCCStrike15_v2_MatchmakingGC2ClientHello <https://github.com/ValvePython/csgo/blob/386b76b17640f7717fe9ead5a6a607e0c821010c/protobufs/cstrike15_gcmessages.proto#L463>`_
        :type message: proto message

        """
        self.send(ECsgoGCMsg.EMsgGCCStrike15_v2_ClientRequestPlayersProfile, {'account_id': account_id,
                                                                              'request_level': request_level,
                                                                              })

    def __handle_player_profile(self: CSGOClient, message):
        if not message.account_profiles:
            return

        self.emit('player_profile', message.account_profiles[0])
