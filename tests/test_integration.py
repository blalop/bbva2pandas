import unittest

from pandas import Timestamp

from bbva2pandas import Report


class TestIntegration(unittest.TestCase):
    FILEPATH = "tests/data/bbva_extract.pdf"

    def test_correct_movement_extraction(self):
        df = Report(self.FILEPATH).to_df()
        movements = df.values.tolist()
        print(movements)
        expected = [
            [
                Timestamp("2022-01-31 00:00:00"),
                Timestamp("2022-01-31 00:00:00"),
                "PAGO CON TARJETA EN SUPERMERCADOS",
                -2.26,
                862.93,
                "4940197136209771",
                "FRUITES \\ VERDURES NAIMA-BARCELONA ES",
            ]
        ]
        self.assertEqual(1, len(movements))
        self.assertEqual(expected, movements)
