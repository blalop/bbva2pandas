# BBVA reports extractor
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Library + script to extract your bank account movements from the pdf reports that BBVA provides each month. Export it to csv or sqlite.

## Dependencies

The following libpoppler dependencies are needed for pdftotext:

```bash
sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
```

## Downloading the reports

In [bbva.es](https://bbva.es), login and go to Posición global > Cuentas y Tarjetas > Ficha. Then click Operaciones > Extracto mensual cuentas. Ready to go!

## Using the libray

Just provide the filepath:

```python
import bbva2pandas
dataframe = bbva2pandas.Report('myfile').to_df()
```


## Running the script

The provided script loads all the PDFs in the provided directory and generates a CSV/sqlite file
```
usage: bbva2pandas [-h] [--output_filename OUTPUT_FILENAME] directory {csv,sqlite}
bbva2pandas: error: the following arguments are required: directory, output_format
```

## Testing

Run

```bash
python3 -m unittest discover tests
```
