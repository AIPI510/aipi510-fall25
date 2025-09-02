import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
response = requests.get(url)
html = response.text


soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", {"class": "wikitable"})

df = pd.read_html(str(table))[0]
df = df.dropna().reset_index(drop=True)

print(df.head())

"""
notes
- this dataset contains nominal GDP by country
- it can be used to compare economic size across nations
- potential uses: economics research, visualization, forecasting
"""
