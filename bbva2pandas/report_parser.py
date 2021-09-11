import re

import pandas as pd


YEAR_FIND_REGEX = re.compile(r'EXTRACTO DE \w* (\d{4})', re.MULTILINE)

MOVEMENTS_PARSE_REGEX = re.compile(
    r'''^
    (\d\d/\d\d) #date
    \s
    (\d\d/\d\d) #value date
    \s*
    ([A-ZÑÁÉÍÓÚÜ\'\,\.\:\s]+) #concept
    \s*
    (-?\d*.?\d*,\d*) #amount of the movement
    \s*
    (\d*.?\d*,\d*) #balance after movement
    \s*
    (\d*) # credit card number
    \s*
    ([\d\wÑÁÉÍÓÚÜ \.\,\:\*\'\-\/\(\)]*) # subconcept
    $''',
    re.MULTILINE | re.IGNORECASE | re.VERBOSE
)

WHITESPACE_REGEX = re.compile(r'\s+')


def _trim_string(col: pd.Series) -> pd.Series:
    """Remove unnecesary whitespaces"""
    return col.apply(lambda x: WHITESPACE_REGEX.sub(' ', x).strip())


def _parse_decimal_separator(col: pd.Series) -> pd.Series:
    """Parses the decimal separator from ',' to '.'"""
    col = col.apply(lambda x: x.replace('.', '').replace(',', '.'))
    return pd.to_numeric(col)


def _format_date(col: pd.Series, year: int) -> pd.Series:
    """Parses the date in Pandas format"""
    return pd.to_datetime(col + '/' + str(year), dayfirst=True)


def parse_report_content(report: str) -> pd.DataFrame:
    """Receives the content of a report and returns a Dataframe"""
    movements = MOVEMENTS_PARSE_REGEX.findall(report)
    year = YEAR_FIND_REGEX.findall(report)[0]

    df = pd.DataFrame(movements, columns=['date', 'value_date', 'concept',
                                          'amount', 'balance',
                                          'card', 'subconcept'])

    df.concept = _trim_string(df.concept)
    df.subconcept = _trim_string(df.subconcept)
    df.date = _format_date(df.date, year)
    df.value_date = _format_date(df.value_date, year)
    df.amount = _parse_decimal_separator(df.amount)
    df.balance = _parse_decimal_separator(df.balance)
    return df
