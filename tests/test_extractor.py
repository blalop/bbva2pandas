import unittest

from bbva2pandas import extractor

class TestExtractor(unittest.TestCase):

    
    def test_year_extraction(self):
        with open('tests/data/pdf-content.txt') as f:
            input = f.read()
        year = extractor.find_year(input)
        self.assertEqual('2050', year)

    def test_movements_extraction(self):
        with open('tests/data/pdf-content.txt') as f:
            input = f.read()
        movements = extractor.find_movements(input)
        expected = [('05/08', '05/08', 'TRANSFERENCIAS                                                                         ', '42,00', '42,00', '', 'X')]
        self.assertEqual(1, len(movements))
        self.assertEqual(expected, movements)
