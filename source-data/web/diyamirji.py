#diyamirji.py

import requests
from bs4 import BeautifulSoup, Comment
import pandas as pd

response = requests.get("https://www.basketball-reference.com/leagues/NBA_2024_totals.html") #to download HTML from the selected page
#data = response.text
#print(data)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find("table", {"id": "totals_stats"})

df = pd.read_html(str(table))[0]
df = df[['Player', 'Age', 'PTS']]
print(df.head())

# this DataFrame holds the table for the top total points for players
# the columns of this DataFrame are the player, age, and total points
# so this data could be used to show if age is relevant to how many points the players will make