import sqlite3
import pandas as pd

def write_tables(countries, borders, currencies, languages):
    """
    Writes into the database

    Args: Four clean dataframes
    """


    con = sqlite3.connect('./data/countries.db')

    countries.to_sql("countries", con, if_exists="replace", index=True)
    borders.to_sql("borders", con, if_exists="replace", index=True)
    currencies.to_sql("currencies", con, if_exists="replace", index=True)
    languages.to_sql("languages", con, if_exists="replace", index=True)