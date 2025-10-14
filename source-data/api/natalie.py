### This is the first assignment for week2 assignment of creating an API 


# 5. Choose an API and read the documentation.
# 6. Write code that:
# - Makes a GET request
# - Parses the JSON response
# - Stores relevant fields into a DataFrame
# 7. Print the first 5 rows of your DataFrame.
# 8. Add 3–5 lines of notes at the bottom of the script describing the data and possible uses.
# 9. Commit


import requests
import json
import pandas as pd


# Load API key from .env file
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API-Key")

# Define the API endpoint and parameters
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

params = {
    "vs_currency": "usd",
    "days": "30",
    "interval": "daily"
}
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Make the GET request
response = requests.get(url, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Extract relevant fields and store in DataFrame

    prices = data.get("prices", [])
    df = pd.DataFrame(prices)
    print(df.head())
else:
    print(f"Failed to retrieve data: {response.status_code}")