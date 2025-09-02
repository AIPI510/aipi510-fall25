import requests
import json
import pandas as pd

# Step 5: choose an API (CoinGecko public API for cryptocurrency markets)
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

# Step 6: make GET request
response = requests.get(url, params=params)
data = response.json()

# Convert JSON into DataFrame with relevant fields
df = pd.DataFrame(data)[["id", "symbol", "current_price", "market_cap", "total_volume"]]

# Step 7: print first 5 rows
print(df.head())

# Step 8: notes
"""
Notes:
This dataset contains cryptocurrency market data from CoinGecko,
including ID, symbol, current price, market cap, and trading volume.
It can be used to track top coins, analyze market movements,
and compare crypto assets by size and liquidity.
"""

