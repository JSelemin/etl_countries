from lib.transform import transform_countries
from lib.extract import fetch_countries
from lib.load import write_tables

def main():
    countries_raw = fetch_countries()
    countries_clean, borders_clean, currencies_clean, languages_clean = transform_countries(countries_raw)
    write_tables(countries_clean, borders_clean, currencies_clean, languages_clean)



if __name__ == "__main__":
    main()