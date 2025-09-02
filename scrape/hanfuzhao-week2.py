import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 5: download HTML from the selected page
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 6: find the desired <table> and parse it into a DataFrame
table = soup.find("table")
df = pd.read_html(str(table))[0]

# Step 6 (clean the data): drop rows with missing values / repeated headers
df = df.dropna()
df = df[df[df.columns[0]] != df.columns[0]]

# Step 7: print the first 5 rows
print(df.head())

# Step 8: notes
"""
Notes:
This dataset lists countries by nominal GDP.
It can be used to compare economies, track changes in rankings,
and study global or regional economic patterns.
"""

