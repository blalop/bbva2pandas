import re

import pandas as pd

DF_COLUMNS = ['date', 'value_date', 'concept',
              'amount', 'balance',
              'card', 'subconcept']


def _trim_string(col: pd.Series) -> pd.Series:
    """Remove unnecesary whitespaces"""
    return col.apply(lambda x: re.sub(r'\s+', ' ', x).strip())


def _transform_decimal_separator(col: pd.Series) -> pd.Series:
    """Parses the decimal separator from ',' to '.'"""
    col = col.apply(lambda x: x.replace('.', '').replace(',', '.'))
    return pd.to_numeric(col)


def _format_date(col: pd.Series, year: str) -> pd.Series:
    """Formats the date in Pandas format"""
    return pd.to_datetime(col + '/' + year, dayfirst=True)


def build_dataframe(movements: list, year: str) -> pd.DataFrame:
    """Builds a dataframe from the report data"""
    df = pd.DataFrame(movements, columns=DF_COLUMNS)

    df.concept = _trim_string(df.concept)
    df.subconcept = _trim_string(df.subconcept)
    df.date = _format_date(df.date, year)
    df.value_date = _format_date(df.value_date, year)
    df.amount = _transform_decimal_separator(df.amount)
    df.balance = _transform_decimal_separator(df.balance)
    return df
