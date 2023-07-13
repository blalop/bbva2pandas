import unittest

from bbva2pandas import extractor


class TestExtractor(unittest.TestCase):
    def test_year_extraction(self):
        with open("tests/data/pdf-content.txt", encoding="utf-8") as f:
            text = f.read()
        year = extractor.find_year(text)
        self.assertEqual("2050", year)

    def test_movements_extraction(self):
        with open("tests/data/pdf-content.txt", encoding="utf-8") as f:
            text = f.read()
        movements = extractor.find_movements(text)
        expected = [
            ("05/08", "05/08", "TRANSFERENCIAS", "42,00", "42,00", "", "X"),
            (
                "12/08",
                "10/08",
                "COMPRA EN COMERCIO EXTRANJERO-COMISIÓN 3 % INCLUÍDA",
                "-8,79",
                "13,55",
                "",
                "LIDL BCN-CAN BATLL\ BARCELONA",
            ),
            ("02/05", "02/05", "TRASPASO", "800,00", "984,57", "", ""),
            (
                "02/05",
                "02/05",
                "TRASPASO",
                "-800,00",
                "184,57",
                "4940197136209771",
                "PERSONA X",
            ),
        ]
        self.assertEqual(4, len(movements))
        self.assertEqual(expected, movements)
