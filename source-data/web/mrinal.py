# imports

import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

html_content = requests.get("https://www.basketball-reference.com/leagues/NBA_2024_totals.html")
if html_content.status_code == 200:
    soup = BeautifulSoup(html_content.text, "html.parser")
    table = soup.find("table")
    df = pd.read_html(str(table))[0]
    print(f"Games with missing Awards - {df.shape}")
    # drop rows if there are no awards
    df = df[df["Awards"].notna() & (df["Awards"].str.strip() != "")]
    print(f"Games with missing Awards Cleaned - {df.shape}")
    print(df.head())
else:
    print("Failed to retrieve the webpage")

'''
My data gets the NBA totals for the 2024 games and then filters the games based on the awards and extracts games which have won awards. I would essentially use this data to do a predictive analysis of which games tend to win awards.
'''


