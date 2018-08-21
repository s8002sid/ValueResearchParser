import xlrd;
import unicodedata;
class ExcelReader(object):
    def __init__(self):
        self.transactionStartPoint = 3;
        self.transactionEndPoint = 0;
    def Read(self, fileName):
        wbook = xlrd.open_workbook(fileName);
        wsheet = wbook.sheet_by_index(0);
        transactions = [];
        for row in range(wsheet.nrows):
            transaction = [];
            for col in range(wsheet.ncols):
                text = wsheet.cell(row, col).value;
                if (type(text) is unicode):
                    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore');
                if (type(text) is float):
                    text = str(text);
                transaction.append(text);
            transactions.append(transaction);
        if (self.transactionStartPoint > 0 and 
            len(transactions) > self.transactionStartPoint):
            del transactions[:self.transactionStartPoint]

        if (self.transactionEndPoint > 0 and
            len(transactions) > self.transactionEndPoint):
            del transactions[(len(transactions)-self.transactionEndPoint):];
        return transactions;