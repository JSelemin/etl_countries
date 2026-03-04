import requests
import pandas as pd


def fetch_countries():
    """
    Extracts data from APICountries

    Returns: Pandas dataframe with raw data
    
    
    """

    x = requests.get('https://www.apicountries.com/countries')

    data = x.json()

    df = pd.DataFrame(data)
    return df