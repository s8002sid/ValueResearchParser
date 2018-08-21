from ExcelReader import *;
from Utility import *;
from FundDetail import *;
class Parser(object):
    def __init__(self, snapshot, returns, portfolio, riskStatus, feesDetails):
        self.snapshot = snapshot;
        self.returns = returns;
        self.portfolio = portfolio;
        self.riskStatus = riskStatus;
        self.feesDetails = feesDetails;
        self.fund = {};
        self.ParseExcel();
    def GetFunds(self):
        return self.fund;

    def ParseExcel(self):
        reader = ExcelReader();
        rows = reader.Read(self.snapshot);
        self.FillSnapshot(rows);
        rows = reader.Read(self.returns);
        self.FillReturns(rows);
        rows = reader.Read(self.portfolio);
        self.FillPortfolio(rows);
        rows = reader.Read(self.riskStatus);
        self.FillRiskStatus(rows);
        rows = reader.Read(self.feesDetails);
        self.FillFeesDetails(rows);

    def FillSnapshot(self, rows):
        #Name
        #Rating
        #Category
        #Launch
        #ExpenseRatio
        #1YearRet
        #1YearRank
        #NetAssetValue
        for i in range(0,len(rows)):
            fundDetail = self.GetFunDetail(rows[i][0]);
            fundDetail.name = rows[i][0];
            fundDetail.rating = rows[i][1].count('*');
            fundDetail.category = rows[i][2];
            fundDetail.launch = Utility.GetDate(rows[i][3]);
            fundDetail.expenseRatio = rows[i][4];
            fundDetail.oneYearReturn = Utility.GetReturn(rows[i][5]);
            fundDetail.oneYearRank = Utility.GetRank(rows[i][6]);
            fundDetail.netAssetValue = rows[i][7];
            self.fund[fundDetail.name] = fundDetail;
    def FillReturns(self, rows):
        #Name
        #Rating
        #1MonthReturn
        #1MonthRank
        #3MonthReturn
        #3MonthRank
        #1YearReturn
        #1YearRank
        #3YearReturn
        #3YearRank
        #5YearReturn
        #5YearRank
        #10YearReturn
        #10YearRank
        for i in range(0,len(rows)):
            fundDetail = self.GetFunDetail(rows[i][0]);
            fundDetail.name = rows[i][0];
            fundDetail.rating = rows[i][1].count('*');
            fundDetail.oneMonthReturn = Utility.GetReturn(rows[i][2]);
            fundDetail.oneMonthRank = Utility.GetRank(rows[i][3]);
            fundDetail.threeMonthReturn = Utility.GetReturn(rows[i][4]);
            fundDetail.threeMonthRank = Utility.GetRank(rows[i][5]);
            fundDetail.oneYearReturn = Utility.GetReturn(rows[i][6]);
            fundDetail.oneYearRank = Utility.GetRank(rows[i][7]);
            fundDetail.threeYearReturn = Utility.GetReturn(rows[i][8]);
            fundDetail.threeYearRank = Utility.GetRank(rows[i][9]);
            fundDetail.fiveYearReturn = Utility.GetReturn(rows[i][10]);
            fundDetail.fiveYearRank = Utility.GetRank(rows[i][11]);
            fundDetail.tenYearReturn = Utility.GetReturn(rows[i][12]);
            fundDetail.tenYearRank = Utility.GetRank(rows[i][13]);
            self.fund[fundDetail.name] = fundDetail;
    def FillPortfolio(self, rows):
        #Name
        #Rating
        #InvestmentStyle
        #Capitalisation
        #MarketCap
        #Turnover
        #CreditQuality
        #InterestRateSensitivity
        #AverageCreditQuality
        #AverageMaturity
        #NetAsset
        for i in range(0,len(rows)):
            fundDetail = self.GetFunDetail(rows[i][0]);
            fundDetail.name = rows[i][0];
            fundDetail.rating = rows[i][1].count('*');
            fundDetail.investmentStyle = Utility.ParseInvestmentStyle(rows[i][2]);
            fundDetail.capitalisation = Utility.ParseCapitalisation(rows[i][3]);
            fundDetail.marketCap = Utility.ParseFloat(rows[i][4]);
            fundDetail.turnOver = Utility.ParseFloat(rows[i][5]);
            fundDetail.creditQuality = rows[i][6];
            fundDetail.interestRateSensitivity = rows[i][7];
            fundDetail.averageCreditQuality = rows[i][8];
            fundDetail.averageMaturity = rows[i][9];
            fundDetail.netAssetValue = Utility.ParseFloat(rows[i][10]);
            self.fund[fundDetail.name] = fundDetail;
    def FillRiskStatus(self, rows):
        #Name
        #Rating
        #FundRiskGrade
        #STD
        #SharpeRatio
        #SortinoRatio
        #Beta
        #Alpha
        #RSquared
        for i in range(0,len(rows)):
            fundDetail = self.GetFunDetail(rows[i][0]);
            fundDetail.name = rows[i][0];
            fundDetail.rating = rows[i][1].count('*');
            fundDetail.fundRiskGrade = rows[i][2];
            fundDetail.STD = Utility.ParseFloat(rows[i][3]);
            fundDetail.sharpeRatio = Utility.ParseFloat(rows[i][4]);
            fundDetail.sortinoRatio = Utility.ParseFloat(rows[i][5]);
            fundDetail.beta = Utility.ParseFloat(rows[i][6]);
            fundDetail.alpha = Utility.ParseFloat(rows[i][7]);
            fundDetail.rSquared = Utility.ParseFloat(rows[i][8]);
            self.fund[fundDetail.name] = fundDetail;
    def FillFeesDetails(self, rows):
        #Name
        #Rating
        #MinimumInvestment
        #ExitLoad
        #ExitPeriod
        #ExpenseRatio
        #PortfolioManager
        #ManagerTenure
        for i in range(0,len(rows)):
            fundDetail = self.GetFunDetail(rows[i][0]);
            fundDetail.name = rows[i][0];
            fundDetail.rating = rows[i][1].count('*');
            fundDetail.minimumInvestment = float(rows[i][2]);
            fundDetail.exitLoad = float(rows[i][3].replace('-', '0').split('(')[0].replace(' ', ''));
            fundDetail.exitPeriod = int(rows[i][3].replace('-', '(0)').split('(')[1].replace(')', '').replace(' ', ''));
            fundDetail.expenseRatio = float(rows[i][4].replace('-', '0.0'));
            value = Utility.ParseFundManager(rows[i][5]);
            fundDetail.manager = value[0];
            fundDetail.managerTanure = value[1];
            self.fund[fundDetail.name] = fundDetail;
    def GetFunDetail(self, key):
        if (key in self.fund.keys()):
            return self.fund[key];
        else:
            return FundDetail();
