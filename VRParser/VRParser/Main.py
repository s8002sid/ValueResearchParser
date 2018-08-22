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
    r'C:\Users\siddjain\Downloads\mf\VR-20180821-SmallCap\snapshot.xls',
    r'C:\Users\siddjain\Downloads\mf\VR-20180821-SmallCap\returns.xls',
    r'C:\Users\siddjain\Downloads\mf\VR-20180821-SmallCap\portfolio.xls',
    r'C:\Users\siddjain\Downloads\mf\VR-20180821-SmallCap\riskStatus.xls',
    r'C:\Users\siddjain\Downloads\mf\VR-20180821-SmallCap\feesDetails.xls'
    );
fund = parser.GetFunds();
fundFilter = LargeCapFundFilter();
fund = fundFilter.Filter(fund);
WriteFundToCSV(fund, 'C:\Users\siddjain\Downloads\mf\VR-20180821-SmallCap\out.csv');
print(len(fund.keys()));
