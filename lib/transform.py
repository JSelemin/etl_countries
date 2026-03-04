import pandas as pd

def transform_countries(df):
    """
    Processes the dataframe intro four clean ones

    Args: Original dataframe

    Returns: Four clean dataframes
    
    """

    countries = df[['alpha3Code', 'name', 'capital', 'subregion', 'region', 'population']]
    borders = df[['alpha3Code', 'borders']]
    currencies = df[['alpha3Code', 'currencies']]
    languages = df[['alpha3Code', 'languages']]
    
    borders = borders.explode('borders', ignore_index=True)

    currencies = currencies.explode('currencies', ignore_index=True)
    alphaCodes = currencies["alpha3Code"]
    currencies = pd.json_normalize(currencies["currencies"])
    currencies['alpha3Code'] = alphaCodes

    languages = languages.explode('languages', ignore_index=True)
    alphaCodes = languages["alpha3Code"]
    languages = pd.json_normalize(languages["languages"])
    languages['alpha3Code'] = alphaCodes

    return countries, borders, currencies, languages