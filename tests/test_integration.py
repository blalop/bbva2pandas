import unittest

from bbva2pandas import pdf, extractor


class TestIntegration(unittest.TestCase):
    FILEPATH = 'data/bbva_extract.pdf'

    def test_correct_movement_extraction(self):
        content = pdf.read_pdf(self.FILEPATH)
        movements = extractor.find_movements(content)
        expected = [('31/01', '31/01', 'PAGO CON TARJETA EN SUPERMERCADOS',
                     '-2,26', '862,93', '4940197136209771', 'FRUITES \ VERDURES NAIMA-BARCELONA      ES')]
        self.assertEqual(1, len(movements))
        self.assertEqual(expected, movements)
