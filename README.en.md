# Global Country Data Pipeline

Small data pipeline that extracts country information from a public REST API, transforms nested JSON data, and loads it into a relational SQLite database structured into four tables. The workflow follows an ETL design (Extract → Transform → Load), using pandas for the transformation stages and enabling further analysis in tools such as Excel or Power BI.

### Technologies

- Python

- pandas

- requests

- SQLite

### Workflow

- Data extraction from a REST API.

- Initial DataFrame fragmentation.

- Conversion and normalization of nested JSON structures.

- Removal of irrelevant columns.

- Creation of relational tables.

- Loading data into SQLite.

## Execution

```bash
pip install -r requirements.txt
python main.py
```

## Database Structure

The database is organized into four tables related through the _alpha3Code_ key.

#### Table: _countries_

Primary Key: alpha3Code

- alpha3Code

- name

- capital

- subregion

- region

- population

#### Table: _borders_

Foreign Key: countries.alpha3Code

- alpha3Code

- borders

#### Table: _currencies_

Foreign Key: countries.alpha3Code

- alpha3Code

- code

- name

- symbol

#### Table: _languages_

Foreign Key: countries.alpha3Code

- alpha3Code

- iso639_1

- iso639_2

- name

- nativeName