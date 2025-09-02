import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.basketball-reference.com/leagues/NBA_2024_totals.html"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

table = soup.find("table", {"id": "totals_stats"})

df = pd.read_html(str(table))[0]
df = df.dropna(how="all")
df = df[df["Rk"] != "Rk"]

print(df.head())

####################################
# This data contains 2023-24 Player Totals stats for the NBA.
# It contains, points, rebounds, assists, and so on. This data
# can be used to calculate player metrics, visualize league leaders,
# and feed the data into ML models for training.
####################################