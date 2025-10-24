### This is the first assignment for week2 assignment of creating a webscraper using BeautifulSoup

# Use requests.get(url) to download HTML from your selected page.
# 6. Use BeautifulSoup to find the desired <table> and parse it into a DataFrame.
# 7. Clean the data (e.g., drop rows with missing values or headers repeated in the table).
# 8. Print the first 5 rows.
# 9. Add 3–5 lines of notes at the bottom of the script describing your data and how you might use it.
# 10. Commit


import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
    
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})
df = pd.read_html(str(table))[0]
df = df.dropna()

print(df.head())