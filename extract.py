#!/usr/bin/env python

import argparse
import glob
import re
import sqlite3

import pandas as pd
import pdftotext
import sqlalchemy


COLUMN_NAMES = ['date', 'value_date', 'concept',
                'amount', 'balance', 'card', 'subconcept']

YEAR_REGEX = re.compile(r'EXTRACTO DE \w* (\d{4})', re.MULTILINE)

OPS_REGEX = re.compile(
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

TRIM_REGEX = re.compile(r'\s+')


def read_report(filename: str) -> str:
    with open(filename, 'rb') as f:
        return '\n'.join(pdftotext.PDF(f))


def parse_report(report: str) -> pd.DataFrame:
    def _trim_str(col: pd.Series) -> pd.Series:
        return col.apply(lambda x: TRIM_REGEX.sub(' ', x).strip())

    def _decimal_separator(col: pd.Series) -> pd.Series:
        return pd.to_numeric(col.apply(lambda x: x.replace('.', '').replace(',', '.')))

    def _format_date(col: pd.Series, year: int) -> pd.Series:
        return pd.to_datetime(col + '/' + str(year), dayfirst=True)

    movements = OPS_REGEX.findall(report)
    year = YEAR_REGEX.findall(report)[0]

    df = pd.DataFrame(movements, columns=COLUMN_NAMES)
    df.concept = _trim_str(df.concept)
    df.subconcept = _trim_str(df.subconcept)
    df.date = _format_date(df.date, year)
    df.value_date = _format_date(df.value_date, year)
    df.amount = _decimal_separator(df.amount)
    df.balance = _decimal_separator(df.balance)
    return df


def extract_directory(dirname: str) -> pd.DataFrame:
    filenames = glob.glob(f'{dirname}/*.pdf')
    if len(filenames) == 0:
        raise ValueError

    reports = map(read_report, filenames)
    dataframes = map(parse_report, reports)
    return pd.concat(dataframes)


def main(directory, output_format, mysql_driver, mysql_string):
    dataframe = extract_directory(directory)
    if output_format == 'csv':
        dataframe.to_csv('movements.csv', sep='|', index=False)
    elif output_format == 'sqlite':
        dataframe.to_sql('MOVEMENTS', sqlite3.connect('movements.db'),
                         if_exists='replace', index=False)
    elif output_format == 'mysql':
        dataframe.to_sql('movements', sqlalchemy.create_engine(
            f'{mysql_driver}://{mysql_string}'),
            if_exists='replace', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Extracts data from BBVA reports PDF files')
    parser.add_argument('directory', help='Directory of the PDF files')
    parser.add_argument('output_format', help='Output format',
                        choices=['csv', 'sqlite', 'mysql'])
    parser.add_argument('--mysql_driver', help='MySQL driver, default: %(default)s',
                        default='mariadb+pymysql')
    parser.add_argument('--mysql_string', help='MySQL connection string, default: %(default)s',
                        default='user:pass@localhost:3306/db')
    args = vars(parser.parse_args())
    main(**args)
