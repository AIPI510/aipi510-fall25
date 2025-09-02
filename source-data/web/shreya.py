import requests
from bs4 import BeautifulSoup
import pandas as pd

data=requests.get("https://www.basketball-reference.com/leagues/NBA_2024_totals.html")
soup=BeautifulSoup(data.text, "html.parser")
table = soup.find("table")
#find and extracted the table using BeautifulSoup
df = pd.read_html(str(table))[0]
df.dropna(inplace=True)
#cleaned the data by dropping the rows with missing values
df.sort_values(by="PTS", ascending=False, inplace=True)
print(df.head(5))
#sorted the data by points and selected the top 10 players

