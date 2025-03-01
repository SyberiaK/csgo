from __future__ import annotations

from typing import TYPE_CHECKING

from csgo.enums import ECsgoGCMsg

if TYPE_CHECKING:
    from csgo.client import CSGOClient


class Match:
    # noinspection PyUnresolvedReferences
    def __init__(self: CSGOClient):
        # register our handlers
        self.on(ECsgoGCMsg.EMsgGCCStrike15_v2_MatchmakingGC2ClientHello, self.__handle_mmstats)
        self.on(ECsgoGCMsg.EMsgGCCStrike15_v2_MatchList, self.__handle_match_list)
        self.on(ECsgoGCMsg.EMsgGCCStrike15_v2_WatchInfoUsers, self.__handle_watch_info)

    def request_matchmaking_stats(self: CSGOClient):
        """
        Request matchmaking statistics

        Response event: ``matchmaking_stats``
        """

        self.send(ECsgoGCMsg.EMsgGCCStrike15_v2_MatchmakingClient2GCHello)

    def __handle_mmstats(self: CSGOClient, message):
        self.emit("matchmaking_stats", message)

    def request_current_live_games(self: CSGOClient):
        """
        Request current live games

        Response event: ``current_live_games``
        """

        self.send(ECsgoGCMsg.EMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames)

    def request_live_game_for_user(self: CSGOClient, account_id):
        """
        .. warning::
            Deprecated. CSGO no longer reponds for this method

        Request recent games for a specific user

        :param account_id: account id of the user
        :type account_id: :class:`int`

        Response event: ``live_game_for_user``
        """
        self.send(ECsgoGCMsg.EMsgGCCStrike15_v2_MatchListRequestLiveGameForUser, {'accountid': account_id})

    def request_full_match_info(self: CSGOClient, matchid, outcomeid, token):
        """
        Request full match info. The parameters can be decoded from a match ShareCode

        :param matchid: match id
        :type matchid: :class:`int`
        :param outcomeid: outcome id
        :type outcomeid: :class:`int`
        :param token: token
        :type token: :class:`int`

        Response event: ``full_match_info``
        """

        self.send(ECsgoGCMsg.EMsgGCCStrike15_v2_MatchListRequestFullGameInfo, {'matchid': matchid,
                                                                               'outcomeid': outcomeid,
                                                                               'token': token})

    def request_recent_user_games(self: CSGOClient, account_id):
        """
        Request recent games for a specific user

        :param account_id: account id of the user
        :type account_id: :class:`int`

        Response event: ``recent_user_games``
        """

        self.send(ECsgoGCMsg.EMsgGCCStrike15_v2_MatchListRequestRecentUserGames, {'accountid': account_id})

    def __handle_match_list(self: CSGOClient, message):
        emsg = message.msgrequestid

        if emsg == ECsgoGCMsg.EMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames:
            self.emit('current_live_games', message)
        elif emsg == ECsgoGCMsg.EMsgGCCStrike15_v2_MatchListRequestLiveGameForUser:
            self.emit('live_game_for_user', message)
        elif emsg == ECsgoGCMsg.EMsgGCCStrike15_v2_MatchListRequestRecentUserGames:
            self.emit('recent_user_games', message)
        elif emsg == ECsgoGCMsg.EMsgGCCStrike15_v2_MatchListRequestFullGameInfo:
            self.emit('full_match_info', message)

    def request_watch_info_friends(self: CSGOClient, account_ids, request_id=1, serverid=0, matchid=0):
        """Request watch info for friends

        :param account_ids: list of account ids
        :type account_ids: list
        :param request_id: request id, used to match reponse with request (default: 1)
        :type request_id: int
        :param serverid: server id
        :type serverid: int
        :param matchid: match id
        :type matchid: int

        Response event: ``watch_info``
        """

        self.send(ECsgoGCMsg.EMsgGCCStrike15_v2_ClientRequestWatchInfoFriends2, {'account_ids': account_ids,
                                                                                 'request_id': request_id,
                                                                                 'serverid': serverid,
                                                                                 'matchid': matchid})

    def __handle_watch_info(self: CSGOClient, message):
        self.emit('watch_info', message)
