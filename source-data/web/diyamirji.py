#diyamirji.py

import requests
from bs4 import BeautifulSoup, Comment
import pandas as pd

#"https://www.york.ac.uk/teaching/cws/wws/webpage1.html"
response = requests.get("https://www.basketball-reference.com/leagues/NBA_2024_totals.html") #to download HTML from the selected page
#data = response.text
#print(data)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find("table", {"id": "totals_stats"})

df = pd.read_html(str(table))[0]
df.head()