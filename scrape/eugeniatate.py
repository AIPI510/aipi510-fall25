"""
Author: Eugenia Tate 
Date: August 30, 2025 

eugeniatate.py 
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_wta_rankings_data():
    """ 
    This method's purpose is to web scrape a wiki page on WTA Tennis rankings. 
    It fetches the data, parses and cleanses it and saves the table in a dataframe.
    The dataframe is being returned by the method to further process data contained in it.  
    
    Parameters: none 
  
    Returns: 
    df - pandas DataFrame 
    """
    # Target URL
    url = "https://en.wikipedia.org/wiki/List_of_WTA_number_1_ranked_singles_tennis_players"

    # Fake a browser User-Agent so Wikipedia doesn't block you
    headers = {"User-Agent": "Mozilla/5.0"} 
    # Fetch the page
    response = requests.get(url, headers=headers)

    # Parse the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract tables
    tables = pd.read_html(response.text)
    df = tables[0]       # pick the very first table on web page
    df["No."] = df["No."].fillna(method="ffill")        #replace NaN with most recent
    df.index = df.index + 1     #change dataframe indexing at 1
    return df


if __name__ == "__main__":
    df = scrape_wta_rankings_data()
    print("Top 5 rows:")
    print(df.head(5))

# Notes:
# This dataset contains the history of #1 ranked female singles tennis players,
# It includes player names, start and end dates of their #1 ranking, and weeks at #1.
# It can be used to analyze dominance of players across eras, compare careers,
# or visualize trends in women's tennis (e.g., most weeks at #1 by country).