import requests
import pandas as pd

URL = "https://www.basketball-reference.com/leagues/NBA_2024_totals.html"

resp = requests.get(URL)
print(resp)
resp.raise_for_status()

df = pd.read_html(resp.text)[0]

df = df[df["Rk"] != "Rk"] #cleaning
df = df.dropna(how="all")

print(df.head())

"""
This dataset has player totals for the 2024 NBA season
Uses:
- You can use this data to compare scoring, assists, rebounds by players
- For creating dashboards
- For your sports analytics projects
"""