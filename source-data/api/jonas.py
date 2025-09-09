import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Build URL for US headlines
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
response = requests.get(url)

# Handle response
if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data['articles'])[['title', 'description', 'url', 'publishedAt', 'source.name']]
    print(df.head(5))
else:
    print(f"Error: {response.status_code}")

# This script fetches US top headlines via NewsAPI into a DataFrame.
# It uses .env for API key security and selects key article fields.
# Output previews first 5 articles, suitable for news alerts or feeds.