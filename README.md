# BBVA reports extractor
[![Build Status](https://travis-ci.com/blalop/accountman.svg?branch=master)](https://travis-ci.com/blalop/accountman)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Script to extract your bank account movements from the pdf reports that BBVA provides each month. Export it to csv, sqlite or mysql.

A [Grafana dashboard](grafana/bank_movements.json) is provided to visualize this data.

## Downloading the reports

In [bbva.es](https://bbva.es), login and go to Posición global > Cuentas y Tarjetas > Ficha. Then click Operaciones > Extracto mensual cuentas. Ready to go!

## Running the script

```
usage: extract.py [-h] [--mysql_driver MYSQL_DRIVER] [--mysql_string MYSQL_STRING] directory {csv,sqlite,mysql}

Extracts data from BBVA reports PDF files

positional arguments:
  directory             Directory of the PDF files
  {csv,sqlite,mysql}    Output format

optional arguments:
  -h, --help            show this help message and exit
  --mysql_driver MYSQL_DRIVER
                        MySQL driver, default: mariadb+pymysql
  --mysql_string MYSQL_STRING
                        MySQL connection string, default: user:pass@localhost:3306/db
```