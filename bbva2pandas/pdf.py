import pdftotext

from bbva2pandas.typing import FilePathOrBuffer


def read_pdf(filepath: FilePathOrBuffer) -> str:
    """Reads the PDF"""
    if isinstance(filepath, str):
        with open(filepath, 'rb') as f:
            return '\n'.join(pdftotext.PDF(f, physical=True))
    else:
        return '\n'.join(pdftotext.PDF(filepath, physical=True))
