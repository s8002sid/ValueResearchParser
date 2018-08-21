from VRParser import *;
from FilterFund import *;
def WriteFundToCSV(fund, filename):
    fob = open(filename, 'w');
    fob.write(FundDetail.CSVHeader() + '\n');
    keys = fund.keys();
    for i in range(0, len(keys)):
        fob.write(fund[keys[i]].CSValue() + '\n')
    fob.close();
parser = Parser(
    r'C:\Users\siddjain\Downloads\mf\snapshot.xls',
    r'C:\Users\siddjain\Downloads\mf\returns.xls',
    r'C:\Users\siddjain\Downloads\mf\portfolio.xls',
    r'C:\Users\siddjain\Downloads\mf\riskStatus.xls',
    r'C:\Users\siddjain\Downloads\mf\feesDetails.xls'
    );
fund = parser.GetFunds();
fund = FilterFund.Filter(fund);
WriteFundToCSV(fund, 'out.csv');
print(len(fund.keys()));
