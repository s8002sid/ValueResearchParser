from enums import *;
from Utility import *;
class FundDetail(object):
    def __init__(self):
        self.name = "";
        self.rating = 0;
        self.category = "";
        self.launch = "";
        self.expenseRatio = 0;
        self.oneMonthReturn = 0;
        self.oneMonthRank = 0;
        self.threeMontReturn = 0;
        self.threeMonthRank = 0;
        self.oneYearReturn = 0;
        self.oneYearRank = 0;
        self.threeYearReturn = 0;
        self.threeYearRank = 0;
        self.fiveYearReturn = 0;
        self.fiveYearRank = 0;
        self.tenYearReturn = 0;
        self.tenYearRank = 0;
        self.netAssetValue = 0;
        self.investmentStyle = InvestmentStyle.none;
        self.capitalisation = Capitalisation.none;
        self.marketCap = 0;
        self.turnOver = 0;
        self.creditQuality = '';
        self.interestRateSensitivity = '';
        self.averageCreditQuality = '';
        self.averageMaturity = '';
        self.fundRiskGrade = '';
        self.STD = 0;
        self.sharpeRatio = 0;
        self.sortinoRatio = 0;
        self.beta = 0;
        self.alpha = 0;
        self.rSquared = 0;
        self.minimumInvestment = 0;
        self.exitLoad = 0;
        self.exitPeriod = 0;
        self.expenseRatio = 0;
        self.manager = '';
        self.managerTanure = 0;
    @staticmethod
    def CSVHeader():
        return "name,"+\
               "rating,"+\
               "category,"+\
               "launch,"+\
               "expenseRatio,"+\
               "oneMonthReturn,"+\
               "oneMonthRank,"+\
               "threeMontReturn,"+\
               "threeMonthRank,"+\
               "oneYearReturn,"+\
               "oneYearRank,"+\
               "threeYearReturn,"+\
               "threeYearRank,"+\
               "fiveYearReturn,"+\
               "fiveYearRank,"+\
               "tenYearReturn,"+\
               "tenYearRank,"+\
               "netAssetValue,"+\
               "investmentStyle,"+\
               "capitalisation,"+\
               "marketCap,"+\
               "turnOver,"+\
               "creditQuality,"+\
               "interestRateSensitivity,"+\
               "averageCreditQuality,"+\
               "averageMaturity,"+\
               "fundRiskGrade,"+\
               "STD,"+\
               "sharpeRatio,"+\
               "sortinoRatio,"+\
               "beta,"+\
               "alpha,"+\
               "rSquared,"+\
               "minimumInvestment,"+\
               "exitLoad,"+\
               "exitPeriod,"+\
               "expenseRatio,"+\
               "manager,"+\
               "managerTanure"
    def CSValue(self):
        return self.name + ',' +\
               str(self.rating) + ',' +\
               self.category + ',' +\
               self.launch + ',' +\
               str(self.expenseRatio) + ',' +\
               str(self.oneMonthReturn) + ',' +\
               str(self.oneMonthRank) + ',' +\
               str(self.threeMontReturn) + ',' +\
               str(self.threeMonthRank) + ',' +\
               str(self.oneYearReturn) + ',' +\
               str(self.oneYearRank) + ',' +\
               str(self.threeYearReturn) + ',' +\
               str(self.threeYearRank) + ',' +\
               str(self.fiveYearReturn) + ',' +\
               str(self.fiveYearRank) + ',' +\
               str(self.tenYearReturn) + ',' +\
               str(self.tenYearRank) + ',' +\
               str(self.netAssetValue) + ',' +\
               Utility.InvestmentstyleToStr(self.investmentStyle) + ',' +\
               Utility.CapitalisationToStr(self.capitalisation) + ',' +\
               str(self.marketCap) + ',' +\
               str(self.turnOver) + ',' +\
               self.creditQuality + ',' +\
               self.interestRateSensitivity + ',' +\
               self.averageCreditQuality + ',' +\
               self.averageMaturity + ',' +\
               self.fundRiskGrade + ',' +\
               str(self.STD) + ',' +\
               str(self.sharpeRatio) + ',' +\
               str(self.sortinoRatio) + ',' +\
               str(self.beta) + ',' +\
               str(self.alpha) + ',' +\
               str(self.rSquared) + ',' +\
               str(self.minimumInvestment) + ',' +\
               str(self.exitLoad) + ',' +\
               str(self.exitPeriod) + ',' +\
               str(self.expenseRatio) + ',' +\
               self.manager + ',' +\
               str(self.managerTanure)