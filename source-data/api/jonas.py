import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv


# load api key from env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       f'apiKey={API_KEY}')
response = requests.get(url)

# parse json and store in pd dataframe
data = response.json()
df = pd.json_normalize(data['articles'])[['title', 'description', 'url', 'publishedAt', 'source.name']]

#print first 5 rows
print(df.head(5))

# This is filtering Title, Description, URL, PublishedAt, Source Name.
# Could be used for quick updates on the most recent news.
# E.g. push the 5 most recent articles to users