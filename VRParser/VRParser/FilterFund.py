from FundDetail import *;
class FundFilter(object):
    def __init__(self):
        self.minManagerExp = 4;
        self.minRating = 3;
        self.minNetAsset = 1000;
        self.maxSTD = 15.5;
        self.minFiveYearRet = 19;
        self.minAlpha = -1;

    def Filter(self, fund):
        fund = self.CheckExperienceOfManager(fund);
        fund = self.FilterStar(fund);
        #fund = self.FilterNetAsset(fund);
        #fund = self.FilterSTD(fund);
        #fund = self.FilterFiveYearReturn(fund);
        #fund = self.FilterAlpha(fund);
        return fund;
    def CheckExperienceOfManager(self, fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].managerTanure < self.minManagerExp):
                del fund[keys[i]];
        return fund;s
    def FilterStar(self, fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].rating < self.minRating and fund[keys[i]].rating != 0):
                del fund[keys[i]];
        return fund;
    def FilterNetAsset(self, fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].netAssetValue < self.minNetAsset):
                del fund[keys[i]];
        return fund;
    def FilterSTD(self, fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].STD >= self.maxSTD):
                del fund[keys[i]];
        return fund;
    def FilterFiveYearReturn(self, fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].fiveYearReturn <= self.minFiveYearRet):
                del fund[keys[i]];
        return fund;
    def FilterAlpha(self, fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].alpha < self.minAlpha):
                del fund[keys[i]];
        return fund;

class LargeCapFundFilter(FundFilter):
    def __init__(self):
        super(LargeCapFundFilter, self).__init__();
        self.minManagerExp = 4;
        self.minRating = 3;
        self.minNetAsset = 1000;
        self.maxSTD = 15.5;
        self.minFiveYearRet = 19;
        self.minAlpha = -1;