import unittest

from bbva2pandas import pdf


class TestExtractor(unittest.TestCase):
    FILEPATH = 'tests/data/abcdef.pdf'

    def test_with_file_open(self):
        with open(self.FILEPATH, 'rb') as f:
            content = pdf.read_pdf(f)
        self.assertEqual('abcdef\n\x0c', content)

    def test_with_file_path(self):
        content = pdf.read_pdf(self.FILEPATH)
        self.assertEqual('abcdef\n\x0c', content)
