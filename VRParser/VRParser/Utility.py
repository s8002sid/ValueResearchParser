from datetime import datetime, timedelta;
from enums import *;
class Utility:
    @staticmethod
    def GetDate(dateStr):
        startDate=datetime(1899,12,30);
        dateDelta = timedelta(int(dateStr.split('.')[0]));
        date = startDate + dateDelta;
        return date.strftime('%d-%m-%Y');
    @staticmethod
    def GetReturn(ret):
        retVal = 0;
        if ('-' not in ret):
            retVal = float(ret);
        return retVal;
    @staticmethod
    def GetRank(rank):
        retVal = '0';
        if ('-' not in rank):
            if ('/' not in rank):
                retVal = float(rank);
                if (retVal > 200):
                    retVal = int(Utility.GetDate(rank).split('-')[1]);
            else:
                retVal = int(rank.split('/')[0]);
        return retVal;
    @staticmethod
    def ParseInvestmentStyle(invStyle):
        if (invStyle == 'Growth'):
            return InvestmentStyle.Growth;
        elif(invStyle == 'Blend'):
            return InvestmentStyle.Blend;
        elif(invStyle == 'Value'):
            return InvestmentStyle.Value;
        else:
            return InvestmentStyle.none;
    @staticmethod
    def ParseCapitalisation(cap):
        if (cap == 'Large Cap'):
            return Capitalisation.Large;
        elif (cap == 'Mid Cap'):
            return Capitalisation.Mid;
        elif (cap == 'Small Cap'):
            return Capitalisation.Small;
        else:
            return Capitalisation.none;
    @staticmethod
    def ParseFloat(value):
        if ('-' == value):
            return 0;
        return float(value);
    @staticmethod
    def ParseFundManager(value):
        mgrs = value.split(',');
        mgr = '';
        exp = 0.0;
        for i in range(0,len(mgrs)):
            m = mgrs[i].split('(')[0];
            e = float(mgrs[i].split('(')[1].replace(')', ''));
            if (e > exp):
                mgr = m;
                exp = e;
        return [mgr, exp];
    
    @staticmethod
    def InvestmentstyleToStr(val):
        if (val == InvestmentStyle.Blend):
            return 'Blend';
        elif(val == InvestmentStyle.Growth):
            return 'Growth';
        elif(val == InvestmentStyle.Value):
            return 'Value';
        else:
            return 'None';
    @staticmethod
    def CapitalisationToStr(val):
        if (val == Capitalisation.Large):
            return 'Large';
        elif(val == Capitalisation.Mid):
            return 'Mid';
        elif(val == Capitalisation.Small):
            return 'Small';
        else:
            return 'None';
