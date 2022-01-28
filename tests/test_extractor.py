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
        expected = [('05/08', '05/08',
                     'TRANSFERENCIAS', '42,00',
                     '42,00', '', 'X'),
                    ('12/08', '10/08', 'COMPRA EN COMERCIO EXTRANJERO-COMISIÓN 3 % INCLUÍDA', '-8,79', '13,55', '',
                     'LIDL BCN-CAN BATLL\ BARCELONA')]
        self.assertEqual(2, len(movements))
        self.assertEqual(expected, movements)
