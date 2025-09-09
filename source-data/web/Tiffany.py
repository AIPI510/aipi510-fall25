import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://newschateau.com/a-look-into-elis-mixology/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

data=[]
# Find the main content div
content_div = soup.find('div', class_='entry-content clear')
if content_div:
    paragraphs = content_div.find_all('p')
    for p in paragraphs:
        print(p.get_text())
        data.append({'interview': p.get_text()})
    df = pd.DataFrame(data)
    print(df)
else:
    print("Content not found.")