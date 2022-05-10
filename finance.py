import yfinance as yf
import datetime


def get_default_start_date():
    date_now = datetime.datetime.now()
    return date_now.replace(date_now.year - 10)


class CompanyStock:
    start_date = None
    end_date = None

    def __init__(self, company_stock_symbol, *, start_date=None, end_date=None):
        self.company = yf.Ticker(company_stock_symbol)
        if start_date is not None:
            self.start_date = start_date
        else:
            self.start_date = get_default_start_date()
        if end_date is not None:
            self.end_date = end_date
        else:
            self.end_date = datetime.datetime.now()

    def get_symbol(self):
        return self.__str__()

    def get_history(self, *, start_date=None, end_date=None):
        if start_date is None:
            start_date = self.start_date

        if end_date is None:
            end_date = self.end_date

        history = self.company.history(start=start_date, end=end_date)
        return history

    def get_item(self, item, *, start_date=None, end_date=None):
        if start_date is None:
            start_date = self.start_date

        if end_date is None:
            end_date = self.end_date

        history = self.get_history(start_date=start_date, end_date=end_date)
        return history.reset_index().get(item)

    def get_open(self, *, start_date=None, end_date=None):
        return self.get_item('Open', start_date=start_date, end_date=end_date)

    def get_high(self, *, start_date=None, end_date=None):
        return self.get_item('High', start_date=start_date, end_date=end_date)

    def get_low(self, *, start_date=None, end_date=None):
        return self.get_item('Low', start_date=start_date, end_date=end_date)

    def get_close(self, *, start_date=None, end_date=None):
        return self.get_item('Close', start_date=start_date, end_date=end_date)

    def get_dividends(self, *, start_date=None, end_date=None):
        return self.get_item('Dividends', start_date=start_date, end_date=end_date)

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def __str__(self):
        return f"Name: {self.company.info['longName']}\nSymbol: {self.company.info['symbol']}"


# Test
if __name__ == '__main__':
    symbol = input('Enter ticker symbol: ')
    company = CompanyStock(symbol)
    print(company)
    print(company.get_symbol())
    company_history = company.get_history()
    print(company_history.head())
    print(company_history.tail())
    print(company.get_open())
    print(company.get_high())
    print(company.get_low())
    print(company.get_close())
    print(company.get_dividends())
