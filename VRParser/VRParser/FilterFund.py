from FundDetail import *;
class FilterFund:
    @staticmethod
    def Filter(fund):
        fund = FilterFund.CheckExperienceOfManager(fund);
        fund = FilterFund.FilterStar(fund);
        fund = FilterFund.FilterNetAsset(fund);
        fund = FilterFund.FilterSTD(fund);
        fund = FilterFund.FilterFiveYearReturn(fund);
        
        return fund;
    @staticmethod
    def CheckExperienceOfManager(fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].managerTanure < 4):
                del fund[keys[i]];
        return fund;
    @staticmethod
    def FilterStar(fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].rating <= 2 and fund[keys[i]].rating != 0):
                del fund[keys[i]];
        return fund;
    @staticmethod
    def FilterNetAsset(fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].netAssetValue < 1000):
                del fund[keys[i]];
        return fund;
    @staticmethod
    def FilterSTD(fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].STD >= 15.5):
                del fund[keys[i]];
        return fund;
    @staticmethod
    def FilterFiveYearReturn(fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].fiveYearReturn <= 19):
                del fund[keys[i]];
        return fund;
    def FilterAlpha(fund):
        keys = fund.keys();
        for i in range(len(keys)-1, -1, -1):
            if (fund[keys[i]].alpha < -1):
                del fund[keys[i]];
        return fund;