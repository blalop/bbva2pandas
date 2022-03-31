import unittest

import pandas as pd
from pandas import Timestamp

from bbva2pandas import dataframe


class TestDataframe(unittest.TestCase):
    def test_trim_string(self):
        original = pd.Series(['a', 'a   b    ', 'a  b  c'])
        expected = ['a', 'a b', 'a b c']
        actual = dataframe._trim_string(original)
        self.assertEqual(expected, actual.to_list())

    def test_transform_decimal_separator(self):
        original = pd.Series(['23,45', '1.500,00'])
        expected = [23.45, 1500]
        actual = dataframe._transform_decimal_separator(original)
        self.assertEqual(expected, actual.to_list())

    def test_format_date(self):
        original = pd.Series(['12/10', '1/1'])
        expected = [Timestamp('2020-10-12 00:00:00'),
                    Timestamp('2020-01-01 00:00:00')]
        actual = dataframe._format_date(original, '2020')
        self.assertEqual(expected, actual.to_list())
