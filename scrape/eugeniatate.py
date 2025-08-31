import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_wta_rankings_data():
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
    print(df.head())