from bbva2pandas.report_parser import parse_report_content

import pandas as pd
import pdftotext

from io import BufferedReader


def read_report(f: BufferedReader) -> pd.DataFrame:
    file_content = '\n'.join(pdftotext.PDF(f))
    return parse_report_content(file_content)
