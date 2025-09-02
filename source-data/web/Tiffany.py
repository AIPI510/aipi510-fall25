import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

data = []

for item in soup.find_all('article', class_='product_pod'):
    title = item.h3.a['title']
    price = item.find('p', class_='price_color').text
    data.append({'title': title, 'price': price})

df = pd.DataFrame(data)
print(df)