import pandas as pd

from bbva2pandas.extractor import find_movements, find_year
from bbva2pandas.pdf import read_pdf
from bbva2pandas.dataframe import build_dataframe
from bbva2pandas.typing import FilePathOrBuffer


class Report:
    def __init__(self, filepath: FilePathOrBuffer) -> None:
        self.content = read_pdf(filepath)
        self.year = find_year(self.content)
        self.movements = find_movements(self.content)

    def to_df(self) -> pd.DataFrame:
        """Receives a filename and parses it to Dataframe"""
        return build_dataframe(self.movements, self.year)
