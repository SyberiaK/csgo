from enum import IntEnum


__all__ = ['ESOType', 'EXPBonusFlag']


class ESOType(IntEnum):
    CSOEconItem = 1
    CSOPersonaDataPublic = 2
    CSOItemRecipe = 5
    CSOEconGameAccountClient = 7
    CSOEconItemDropRateBonus = 38
    CSOEconItemEventTicket = 40
    CSOAccountSeasonalOperation = 41
    CSOEconDefaultEquippedDefinitionInstanceClient = 43
    CSOEconCoupon = 45
    CSOQuestProgress = 46


class EXPBonusFlag(IntEnum):
    EarnedXpThisPeriod = 1 << 0
    FirstReward = 1 << 1
    Msg_YourReportGotConvicted = 1 << 2
    Msg_YouPartiedWithCheaters = 1 << 3
    PrestigeEarned = 1 << 4
    ChinaGovernmentCert = 1 << 5
    OverwatchBonus = 1 << 28
    BonusBoostConsumed = 1 << 29
    ReducedGain = 1 << 30
