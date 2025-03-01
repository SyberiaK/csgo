from enum import IntEnum


__all__ = ['EClientReportingVersion',
           'ECommunityItemAttribute',
           'ECommunityItemClass',
           'ECsgoGCMsg',
           'ECsgoSteamUserStat',
           'EGCBaseClientMsg',
           'EGCItemCustomizationNotification',
           'EGCItemMsg',
           'EGCMsgResponse',
           'EGCSystemMsg',
           'EGCToGCMsg',
           'ESOMsg',
           'EUnlockStyle',
           'GCClientLauncherType',
           'GCConnectionStatus',]


class EClientReportingVersion(IntEnum):
    OldVersion = 0
    BetaVersion = 1
    SupportsTrustedMode = 2


class ECommunityItemAttribute(IntEnum):
    Invalid = 0
    CardBorder = 1
    Level = 2
    IssueNumber = 3
    TradableTime = 4
    StorePackageID = 5
    CommunityItemAppID = 6
    CommunityItemType = 7
    ProfileModiferEnabled = 8
    ExpiryTime = 9


class ECommunityItemClass(IntEnum):
    Invalid = 0
    Badge = 1
    GameCard = 2
    ProfileBackground = 3
    Emoticon = 4
    BoosterPack = 5
    Consumable = 6
    GameGoo = 7
    ProfileModifier = 8
    Scene = 9
    SalienItem = 10


class ECsgoGCMsg(IntEnum):
    EMsgGCCStrike15_v2_Base = 9100
    EMsgGCCStrike15_v2_MatchmakingStart = 9101
    EMsgGCCStrike15_v2_MatchmakingStop = 9102
    EMsgGCCStrike15_v2_MatchmakingClient2ServerPing = 9103
    EMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate = 9104
    EMsgGCCStrike15_v2_MatchmakingServerReservationResponse = 9106
    EMsgGCCStrike15_v2_MatchmakingGC2ClientReserve = 9107
    EMsgGCCStrike15_v2_MatchmakingClient2GCHello = 9109
    EMsgGCCStrike15_v2_MatchmakingGC2ClientHello = 9110
    EMsgGCCStrike15_v2_MatchmakingGC2ClientAbandon = 9112
    EMsgGCCStrike15_v2_MatchmakingGCOperationalStats = 9115
    EMsgGCCStrike15_v2_MatchmakingOperator2GCBlogUpdate = 9117
    EMsgGCCStrike15_v2_ServerNotificationForUserPenalty = 9118
    EMsgGCCStrike15_v2_ClientReportPlayer = 9119
    EMsgGCCStrike15_v2_ClientReportServer = 9120
    EMsgGCCStrike15_v2_ClientCommendPlayer = 9121
    EMsgGCCStrike15_v2_ClientReportResponse = 9122
    EMsgGCCStrike15_v2_ClientCommendPlayerQuery = 9123
    EMsgGCCStrike15_v2_ClientCommendPlayerQueryResponse = 9124
    EMsgGCCStrike15_v2_WatchInfoUsers = 9126
    EMsgGCCStrike15_v2_ClientRequestPlayersProfile = 9127
    EMsgGCCStrike15_v2_PlayersProfile = 9128
    EMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate = 9131
    EMsgGCCStrike15_v2_PlayerOverwatchCaseAssignment = 9132
    EMsgGCCStrike15_v2_PlayerOverwatchCaseStatus = 9133
    EMsgGCCStrike15_v2_GC2ClientTextMsg = 9134
    EMsgGCCStrike15_v2_Client2GCTextMsg = 9135
    EMsgGCCStrike15_v2_MatchEndRunRewardDrops = 9136
    EMsgGCCStrike15_v2_MatchEndRewardDropsNotification = 9137
    EMsgGCCStrike15_v2_ClientRequestWatchInfoFriends2 = 9138
    EMsgGCCStrike15_v2_MatchList = 9139
    EMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames = 9140
    EMsgGCCStrike15_v2_MatchListRequestRecentUserGames = 9141
    EMsgGCCStrike15_v2_GC2ServerReservationUpdate = 9142
    EMsgGCCStrike15_v2_ClientVarValueNotificationInfo = 9144
    EMsgGCCStrike15_v2_MatchListRequestTournamentGames = 9146
    EMsgGCCStrike15_v2_MatchListRequestFullGameInfo = 9147
    EMsgGCCStrike15_v2_GiftsLeaderboardRequest = 9148
    EMsgGCCStrike15_v2_GiftsLeaderboardResponse = 9149
    EMsgGCCStrike15_v2_ServerVarValueNotificationInfo = 9150
    EMsgGCCStrike15_v2_ClientSubmitSurveyVote = 9152
    EMsgGCCStrike15_v2_Server2GCClientValidate = 9153
    EMsgGCCStrike15_v2_MatchListRequestLiveGameForUser = 9154
    EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockRequest = 9156
    EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse = 9157
    EMsgGCCStrike15_v2_AccountPrivacySettings = 9158
    EMsgGCCStrike15_v2_SetMyActivityInfo = 9159
    EMsgGCCStrike15_v2_MatchListRequestTournamentPredictions = 9160
    EMsgGCCStrike15_v2_MatchListUploadTournamentPredictions = 9161
    EMsgGCCStrike15_v2_DraftSummary = 9162
    EMsgGCCStrike15_v2_ClientRequestJoinFriendData = 9163
    EMsgGCCStrike15_v2_ClientRequestJoinServerData = 9164
    EMsgGCCStrike15_v2_ClientRequestNewMission = 9165
    EMsgGCCStrike15_v2_GC2ClientTournamentInfo = 9167
    EMsgGC_GlobalGame_Subscribe = 9168
    EMsgGC_GlobalGame_Unsubscribe = 9169
    EMsgGC_GlobalGame_Play = 9170
    EMsgGCCStrike15_v2_AcknowledgePenalty = 9171
    EMsgGCCStrike15_v2_Client2GCRequestPrestigeCoin = 9172
    EMsgGCCStrike15_v2_GC2ClientGlobalStats = 9173
    EMsgGCCStrike15_v2_Client2GCStreamUnlock = 9174
    EMsgGCCStrike15_v2_FantasyRequestClientData = 9175
    EMsgGCCStrike15_v2_FantasyUpdateClientData = 9176
    EMsgGCCStrike15_v2_GCToClientSteamdatagramTicket = 9177
    EMsgGCCStrike15_v2_ClientToGCRequestTicket = 9178
    EMsgGCCStrike15_v2_ClientToGCRequestElevate = 9179
    EMsgGCCStrike15_v2_GlobalChat = 9180
    EMsgGCCStrike15_v2_GlobalChat_Subscribe = 9181
    EMsgGCCStrike15_v2_GlobalChat_Unsubscribe = 9182
    EMsgGCCStrike15_v2_ClientAuthKeyCode = 9183
    EMsgGCCStrike15_v2_GotvSyncPacket = 9184
    EMsgGCCStrike15_v2_ClientPlayerDecalSign = 9185
    EMsgGCCStrike15_v2_ClientLogonFatalError = 9187
    EMsgGCCStrike15_v2_ClientPollState = 9188
    EMsgGCCStrike15_v2_Party_Register = 9189
    EMsgGCCStrike15_v2_Party_Unregister = 9190
    EMsgGCCStrike15_v2_Party_Search = 9191
    EMsgGCCStrike15_v2_Party_Invite = 9192
    EMsgGCCStrike15_v2_Account_RequestCoPlays = 9193
    EMsgGCCStrike15_v2_ClientGCRankUpdate = 9194
    EMsgGCCStrike15_v2_ClientRequestOffers = 9195
    EMsgGCCStrike15_v2_ClientAccountBalance = 9196
    EMsgGCCStrike15_v2_ClientPartyJoinRelay = 9197
    EMsgGCCStrike15_v2_ClientPartyWarning = 9198
    EMsgGCCStrike15_v2_SetEventFavorite = 9200
    EMsgGCCStrike15_v2_GetEventFavorites_Request = 9201
    EMsgGCCStrike15_v2_ClientPerfReport = 9202
    EMsgGCCStrike15_v2_GetEventFavorites_Response = 9203
    EMsgGCCStrike15_v2_ClientRequestSouvenir = 9204
    EMsgGCCStrike15_v2_ClientReportValidation = 9205
    EMsgGCCStrike15_v2_GC2ClientRefuseSecureMode = 9206
    EMsgGCCStrike15_v2_GC2ClientRequestValidation = 9207
    EMsgGCCStrike15_v2_ClientRedeemMissionReward = 9209
    EMsgGCCStrike15_ClientDeepStats = 9210
    EMsgGCCStrike15_StartAgreementSessionInGame = 9211


class ECsgoSteamUserStat(IntEnum):
    XpEarnedGames = 1
    MatchWinsCompetitive = 2
    SurvivedDangerZone = 3


class EGCBaseClientMsg(IntEnum):
    EMsgGCClientWelcome = 4004
    EMsgGCServerWelcome = 4005
    EMsgGCClientHello = 4006
    EMsgGCServerHello = 4007
    EMsgGCClientConnectionStatus = 4009
    EMsgGCServerConnectionStatus = 4010
    EMsgGCClientHelloPartner = 4011
    EMsgGCClientHelloPW = 4012
    EMsgGCClientHelloR2 = 4013
    EMsgGCClientHelloR3 = 4014
    EMsgGCClientHelloR4 = 4015


class EGCItemCustomizationNotification(IntEnum):
    NameItem = 1006
    UnlockCrate = 1007
    XRayItemReveal = 1008
    XRayItemClaim = 1009
    CasketTooFull = 1011
    CasketContents = 1012
    CasketAdded = 1013
    CasketRemoved = 1014
    CasketInvFull = 1015
    NameBaseItem = 1019
    RemoveItemName = 1030
    RemoveSticker = 1053
    ApplySticker = 1086
    StatTrakSwap = 1088
    RemovePatch = 1089
    ApplyPatch = 1090
    ActivateFanToken = 9178
    ActivateOperationCoin = 9179
    GraffitiUnseal = 9185
    GenerateSouvenir = 9204
    ClientRedeemMissionReward = 9209


class EGCItemMsg(IntEnum):
    EMsgGCBase = 1000
    EMsgGCSetItemPosition = 1001
    EMsgGCCraft = 1002
    EMsgGCCraftResponse = 1003
    EMsgGCDelete = 1004
    EMsgGCVerifyCacheSubscription = 1005
    EMsgGCNameItem = 1006
    EMsgGCUnlockCrate = 1007
    EMsgGCUnlockCrateResponse = 1008
    EMsgGCPaintItem = 1009
    EMsgGCPaintItemResponse = 1010
    EMsgGCGoldenWrenchBroadcast = 1011
    EMsgGCMOTDRequest = 1012
    EMsgGCMOTDRequestResponse = 1013
    EMsgGCAddItemToSocket_DEPRECATED = 1014
    EMsgGCAddItemToSocketResponse_DEPRECATED = 1015
    EMsgGCAddSocketToBaseItem_DEPRECATED = 1016
    EMsgGCAddSocketToItem_DEPRECATED = 1017
    EMsgGCAddSocketToItemResponse_DEPRECATED = 1018
    EMsgGCNameBaseItem = 1019
    EMsgGCNameBaseItemResponse = 1020
    EMsgGCRemoveSocketItem_DEPRECATED = 1021
    EMsgGCRemoveSocketItemResponse_DEPRECATED = 1022
    EMsgGCCustomizeItemTexture = 1023
    EMsgGCCustomizeItemTextureResponse = 1024
    EMsgGCUseItemRequest = 1025
    EMsgGCUseItemResponse = 1026
    EMsgGCGiftedItems_DEPRECATED = 1027
    EMsgGCRemoveItemName = 1030
    EMsgGCRemoveItemPaint = 1031
    EMsgGCGiftWrapItem = 1032
    EMsgGCGiftWrapItemResponse = 1033
    EMsgGCDeliverGift = 1034
    EMsgGCDeliverGiftResponseGiver = 1035
    EMsgGCDeliverGiftResponseReceiver = 1036
    EMsgGCUnwrapGiftRequest = 1037
    EMsgGCUnwrapGiftResponse = 1038
    EMsgGCSetItemStyle = 1039
    EMsgGCUsedClaimCodeItem = 1040
    EMsgGCSortItems = 1041
    EMsgGC_RevolvingLootList_DEPRECATED = 1042
    EMsgGCLookupAccount = 1043
    EMsgGCLookupAccountResponse = 1044
    EMsgGCLookupAccountName = 1045
    EMsgGCLookupAccountNameResponse = 1046
    EMsgGCUpdateItemSchema = 1049
    EMsgGCRemoveCustomTexture = 1051
    EMsgGCRemoveCustomTextureResponse = 1052
    EMsgGCRemoveMakersMark = 1053
    EMsgGCRemoveMakersMarkResponse = 1054
    EMsgGCRemoveUniqueCraftIndex = 1055
    EMsgGCRemoveUniqueCraftIndexResponse = 1056
    EMsgGCSaxxyBroadcast = 1057
    EMsgGCBackpackSortFinished = 1058
    EMsgGCAdjustItemEquippedState = 1059
    EMsgGCCollectItem = 1061
    EMsgGCItemAcknowledged__DEPRECATED = 1062
    EMsgGC_ReportAbuse = 1065
    EMsgGC_ReportAbuseResponse = 1066
    EMsgGCNameItemNotification = 1068
    EMsgGCApplyConsumableEffects = 1069
    EMsgGCConsumableExhausted = 1070
    EMsgGCShowItemsPickedUp = 1071
    EMsgGCClientDisplayNotification = 1072
    EMsgGCApplyStrangePart = 1073
    EMsgGC_IncrementKillCountAttribute = 1074
    EMsgGC_IncrementKillCountResponse = 1075
    EMsgGCApplyPennantUpgrade = 1076
    EMsgGCSetItemPositions = 1077
    EMsgGCApplyEggEssence = 1078
    EMsgGCNameEggEssenceResponse = 1079
    EMsgGCPaintKitItem = 1080
    EMsgGCPaintKitBaseItem = 1081
    EMsgGCPaintKitItemResponse = 1082
    EMsgGCGiftedItems = 1083
    EMsgGCUnlockItemStyle = 1084
    EMsgGCUnlockItemStyleResponse = 1085
    EMsgGCApplySticker = 1086
    EMsgGCItemAcknowledged = 1087
    EMsgGCStatTrakSwap = 1088
    EMsgGCUserTrackTimePlayedConsecutively = 1089
    EMsgGCItemCustomizationNotification = 1090
    EMsgGCModifyItemAttribute = 1091
    EMsgGCCasketItemAdd = 1092
    EMsgGCCasketItemExtract = 1093
    EMsgGCCasketItemLoadContents = 1094
    EMsgGCTradingBase = 1500
    EMsgGCTrading_InitiateTradeRequest = 1501
    EMsgGCTrading_InitiateTradeResponse = 1502
    EMsgGCTrading_StartSession = 1503
    EMsgGCTrading_SetItem = 1504
    EMsgGCTrading_RemoveItem = 1505
    EMsgGCTrading_UpdateTradeInfo = 1506
    EMsgGCTrading_SetReadiness = 1507
    EMsgGCTrading_ReadinessResponse = 1508
    EMsgGCTrading_SessionClosed = 1509
    EMsgGCTrading_CancelSession = 1510
    EMsgGCTrading_TradeChatMsg = 1511
    EMsgGCTrading_ConfirmOffer = 1512
    EMsgGCTrading_TradeTypingChatMsg = 1513
    EMsgGCServerBrowser_FavoriteServer = 1601
    EMsgGCServerBrowser_BlacklistServer = 1602
    EMsgGCServerRentalsBase = 1700
    EMsgGCItemPreviewCheckStatus = 1701
    EMsgGCItemPreviewStatusResponse = 1702
    EMsgGCItemPreviewRequest = 1703
    EMsgGCItemPreviewRequestResponse = 1704
    EMsgGCItemPreviewExpire = 1705
    EMsgGCItemPreviewExpireNotification = 1706
    EMsgGCItemPreviewItemBoughtNotification = 1707
    EMsgGCDev_NewItemRequest = 2001
    EMsgGCDev_NewItemRequestResponse = 2002
    EMsgGCDev_PaintKitDropItem = 2003
    EMsgGCStoreGetUserData = 2500
    EMsgGCStoreGetUserDataResponse = 2501
    EMsgGCStorePurchaseInit_DEPRECATED = 2502
    EMsgGCStorePurchaseInitResponse_DEPRECATED = 2503
    EMsgGCStorePurchaseFinalize = 2504
    EMsgGCStorePurchaseFinalizeResponse = 2505
    EMsgGCStorePurchaseCancel = 2506
    EMsgGCStorePurchaseCancelResponse = 2507
    EMsgGCStorePurchaseQueryTxn = 2508
    EMsgGCStorePurchaseQueryTxnResponse = 2509
    EMsgGCStorePurchaseInit = 2510
    EMsgGCStorePurchaseInitResponse = 2511
    EMsgGCBannedWordListRequest = 2512
    EMsgGCBannedWordListResponse = 2513
    EMsgGCToGCBannedWordListBroadcast = 2514
    EMsgGCToGCBannedWordListUpdated = 2515
    EMsgGCToGCDirtySDOCache = 2516
    EMsgGCToGCDirtyMultipleSDOCache = 2517
    EMsgGCToGCUpdateSQLKeyValue = 2518
    EMsgGCToGCIsTrustedServer = 2519
    EMsgGCToGCIsTrustedServerResponse = 2520
    EMsgGCToGCBroadcastConsoleCommand = 2521
    EMsgGCServerVersionUpdated = 2522
    EMsgGCApplyAutograph = 2523
    EMsgGCToGCWebAPIAccountChanged = 2524
    EMsgGCRequestAnnouncements = 2525
    EMsgGCRequestAnnouncementsResponse = 2526
    EMsgGCRequestPassportItemGrant = 2527
    EMsgGCClientVersionUpdated = 2528
    EMsgGCAdjustItemEquippedStateMulti = 2529


class EGCMsgResponse(IntEnum):
    EGCMsgResponseOK = 0
    EGCMsgResponseDenied = 1
    EGCMsgResponseServerError = 2
    EGCMsgResponseTimeout = 3
    EGCMsgResponseInvalid = 4
    EGCMsgResponseNoMatch = 5
    EGCMsgResponseUnknownError = 6
    EGCMsgResponseNotLoggedOn = 7
    EGCMsgFailedToCreate = 8
    EGCMsgLimitExceeded = 9
    EGCMsgCommitUnfinalized = 10


class EGCSystemMsg(IntEnum):
    EGCMsgInvalid = 0
    EGCMsgMulti = 1
    EGCMsgGenericReply = 10
    EGCMsgSystemBase = 50
    EGCMsgAchievementAwarded = 51
    EGCMsgConCommand = 52
    EGCMsgStartPlaying = 53
    EGCMsgStopPlaying = 54
    EGCMsgStartGameserver = 55
    EGCMsgStopGameserver = 56
    EGCMsgWGRequest = 57
    EGCMsgWGResponse = 58
    EGCMsgGetUserGameStatsSchema = 59
    EGCMsgGetUserGameStatsSchemaResponse = 60
    EGCMsgGetUserStatsDEPRECATED = 61
    EGCMsgGetUserStatsResponse = 62
    EGCMsgAppInfoUpdated = 63
    EGCMsgValidateSession = 64
    EGCMsgValidateSessionResponse = 65
    EGCMsgLookupAccountFromInput = 66
    EGCMsgSendHTTPRequest = 67
    EGCMsgSendHTTPRequestResponse = 68
    EGCMsgPreTestSetup = 69
    EGCMsgRecordSupportAction = 70
    EGCMsgGetAccountDetails_DEPRECATED = 71
    EGCMsgReceiveInterAppMessage = 73
    EGCMsgFindAccounts = 74
    EGCMsgPostAlert = 75
    EGCMsgGetLicenses = 76
    EGCMsgGetUserStats = 77
    EGCMsgGetCommands = 78
    EGCMsgGetCommandsResponse = 79
    EGCMsgAddFreeLicense = 80
    EGCMsgAddFreeLicenseResponse = 81
    EGCMsgGetIPLocation = 82
    EGCMsgGetIPLocationResponse = 83
    EGCMsgSystemStatsSchema = 84
    EGCMsgGetSystemStats = 85
    EGCMsgGetSystemStatsResponse = 86
    EGCMsgSendEmail = 87
    EGCMsgSendEmailResponse = 88
    EGCMsgGetEmailTemplate = 89
    EGCMsgGetEmailTemplateResponse = 90
    EGCMsgGrantGuestPass = 91
    EGCMsgGrantGuestPassResponse = 92
    EGCMsgGetAccountDetails = 93
    EGCMsgGetAccountDetailsResponse = 94
    EGCMsgGetPersonaNames = 95
    EGCMsgGetPersonaNamesResponse = 96
    EGCMsgMultiplexMsg = 97
    EGCMsgMultiplexMsgResponse = 98
    EGCMsgWebAPIRegisterInterfaces = 101
    EGCMsgWebAPIJobRequest = 102
    EGCMsgWebAPIJobRequestHttpResponse = 104
    EGCMsgWebAPIJobRequestForwardResponse = 105
    EGCMsgMemCachedGet = 200
    EGCMsgMemCachedGetResponse = 201
    EGCMsgMemCachedSet = 202
    EGCMsgMemCachedDelete = 203
    EGCMsgMemCachedStats = 204
    EGCMsgMemCachedStatsResponse = 205
    EGCMsgMasterSetDirectory = 220
    EGCMsgMasterSetDirectoryResponse = 221
    EGCMsgMasterSetWebAPIRouting = 222
    EGCMsgMasterSetWebAPIRoutingResponse = 223
    EGCMsgMasterSetClientMsgRouting = 224
    EGCMsgMasterSetClientMsgRoutingResponse = 225
    EGCMsgSetOptions = 226
    EGCMsgSetOptionsResponse = 227
    EGCMsgSystemBase2 = 500
    EGCMsgGetPurchaseTrustStatus = 501
    EGCMsgGetPurchaseTrustStatusResponse = 502
    EGCMsgUpdateSession = 503
    EGCMsgGCAccountVacStatusChange = 504
    EGCMsgCheckFriendship = 505
    EGCMsgCheckFriendshipResponse = 506
    EGCMsgGetPartnerAccountLink = 507
    EGCMsgGetPartnerAccountLinkResponse = 508
    EGCMsgDPPartnerMicroTxns = 512
    EGCMsgDPPartnerMicroTxnsResponse = 513
    EGCMsgVacVerificationChange = 518
    EGCMsgAccountPhoneNumberChange = 519
    EGCMsgInviteUserToLobby = 523
    EGCMsgGetGamePersonalDataCategoriesRequest = 524
    EGCMsgGetGamePersonalDataCategoriesResponse = 525
    EGCMsgGetGamePersonalDataEntriesRequest = 526
    EGCMsgGetGamePersonalDataEntriesResponse = 527
    EGCMsgTerminateGamePersonalDataEntriesRequest = 528
    EGCMsgTerminateGamePersonalDataEntriesResponse = 529


class EGCToGCMsg(IntEnum):
    EGCToGCMsgMasterAck = 150
    EGCToGCMsgMasterAckResponse = 151
    EGCToGCMsgRouted = 152
    EGCToGCMsgRoutedReply = 153
    EMsgUpdateSessionIP = 154
    EMsgRequestSessionIP = 155
    EMsgRequestSessionIPResponse = 156
    EGCToGCMsgMasterStartupComplete = 157


class ESOMsg(IntEnum):
    Create = 21
    Update = 22
    Destroy = 23
    CacheSubscribed = 24
    CacheUnsubscribed = 25
    UpdateMultiple = 26
    CacheSubscriptionCheck = 27
    CacheSubscriptionRefresh = 28


class EUnlockStyle(IntEnum):
    UnlockStyle_Succeeded = 0
    UnlockStyle_Failed_PreReq = 1
    UnlockStyle_Failed_CantAfford = 2
    UnlockStyle_Failed_CantCommit = 3
    UnlockStyle_Failed_CantLockCache = 4
    UnlockStyle_Failed_CantAffordAttrib = 5


class GCClientLauncherType(IntEnum):
    DEFAULT = 0
    PERFECTWORLD = 1
    STEAMCHINA = 2


class GCConnectionStatus(IntEnum):
    HAVE_SESSION = 0
    GC_GOING_DOWN = 1
    NO_SESSION = 2
    NO_SESSION_IN_LOGON_QUEUE = 3
    NO_STEAM = 4
