import unittest
import pandas as pd

from pandas._libs.tslibs.timestamps import Timestamp
from bbva2pandas import report_parser


class TestReportParser(unittest.TestCase):
    def test_trim_string(self):
        original = pd.Series(['a', 'a   b', 'a  b  c'])
        expected = ['a', 'a b', 'a b c']
        actual = report_parser._trim_string(original)
        self.assertEqual(expected, actual.to_list())

    def test_parse_decimal_separator(self):
        original = pd.Series(['23,45', '1.500,00'])
        expected = [23.45, 1500]
        actual = report_parser._parse_decimal_separator(original)
        self.assertEqual(expected, actual.to_list())

    def test_format_date(self):
        original = pd.Series(['12/10', '1/1'])
        expected = [Timestamp('2020-10-12 00:00:00'),
                    Timestamp('2020-01-01 00:00:00')]
        actual = report_parser._format_date(original, 2020)
        self.assertEqual(expected, actual.to_list())

    def test_parse_report_content(self):
        with open('tests/data/pdf-content.txt') as f:
            input = f.read()
        actual = report_parser.parse_report_content(input)
        first = actual.iloc[0]
        self.assertEqual(1, actual.shape[0])
        self.assertEqual(Timestamp('2050-08-05 00:00:00'), first.date)
        self.assertEqual(Timestamp('2050-08-05 00:00:00'), first.value_date)
        self.assertEqual('TRANSFERENCIAS', first.concept)
        self.assertEqual(42, first.amount)
        self.assertEqual(42, first.balance)
        self.assertEqual('X', first.subconcept)
