import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.basketball-reference.com/leagues/NBA_2024_totals.html")
soup = BeautifulSoup(r.text, 'html.parser')

raw_table = soup.find("table", {"id": "totals_stats"})
# print(raw_table)

headers = [th["data-stat"] for th in raw_table.find("thead").find_all("th")]

rows = []
for row in raw_table.find("tbody").find_all("tr"):
    cells = [row.find("th").text] + [td.text for td in row.find_all("td")]
    rows.append(cells)

df = pd.DataFrame(rows, columns=headers)
print(headers)
df = df.drop(columns=["ranker", "age", "team_name_abbr", "pos", "games", "games_started", "orb", "drb", "trb", "ast", "stl", "blk", "tov", "pf", "tpl_dbl", "awards"]) # drop all columnsnot related to scoring
df = df.dropna() # drop all rows with missing cells that relate to scoring
df = df.drop(df.index[-1]) # drop league average row
print(df.head(5))
print(df.isna().any().any())

"""
The data provided here is name and all scoring stats (totals and percentages)
This data couple be used to train a model that fills in missing stats with machine learning logic
The data does not contain rows with missing values in scoring or name columns
"""