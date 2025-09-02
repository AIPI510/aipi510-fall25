import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://github.com/trending'

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

div_list = soup.find_all('div', attrs={'data-hpc': True})
print(div_list)

df = pd.DataFrame({'articles': div_list})

# Data could be used to find popular articles that are currently trending
