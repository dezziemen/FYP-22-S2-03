import datetime
import unittest
from finance import CompanyStock
from pandas import DataFrame, Series


class CompanyStockTest(unittest.TestCase):
    test_ticker = 'AAPL'
    company = CompanyStock(test_ticker)

    def test_get_symbol(self):
        self.assertEqual(self.company.get_symbol(), self.test_ticker)

    def test_get_history(self):
        self.assertIsInstance(self.company.get_history(), DataFrame)

    def test_get_open(self):
        self.assertIsInstance(self.company.get_open(), Series)

    def test_get_high(self):
        self.assertIsInstance(self.company.get_high(), Series)

    def test_get_low(self):
        self.assertIsInstance(self.company.get_low(), Series)

    def test_get_close(self):
        self.assertIsInstance(self.company.get_close(), Series)

    def test_set_start_date(self):
        start_date = datetime.datetime.now().replace(datetime.datetime.now().year - 2)
        self.company.set_start_date(start_date)


if __name__ == '__main__':
    unittest.main()
