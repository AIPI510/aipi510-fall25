import requests

from bs4 import BeautifulSoup
import pandas as pd


url="https://en.wikipedia.org/wiki/List_of_NBA_champions"

headers = {
        'User-Agent': "AIPIclassactivity (alex.oh@duke.edu)"
}

response = requests.get(url,headers=headers)

# print(response.headers, response.status_code,response.text)

soup = BeautifulSoup(response.text,'html.parser')


table = soup.find('table', class_ = 'wikitable sortable sticky-header')

# print(table)
headers = [th.text.strip() for th in table.find_all('th')]
rows_data = []

for row in table.find_all('tr'):
    cells = [td.text.strip() for td in row.find_all('td')]
    if cells:
        rows_data.append(cells)
# print(rows_data)

df = pd.DataFrame(rows_data)
df.columns = headers
print(df.info(), df.describe())
df.to_csv("alex_nba_data.csv")

# I could use this data for sports related tasks like the prediction of future champions
