import requests
#import json
import pandas as pd
import os
from dotenv import load_dotenv

# Load API key from .env file, to keep it private.
load_dotenv()
API_KEY = os.getenv("API_KEY")

# calls CoinGecko API to get list of top coins and returns a dataframe with basic market data
def get_top_coin_list(top=10):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": top,
        "x_cg_demo_api_key": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    response.raise_for_status()

    df = pd.json_normalize(data)
    return df

# calls CoinGecko API to get prices of list of coin with given id
def get_current_price(coins):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "vs_currencies": "usd",
        "ids": ",".join(coins),
        "include_market_cap": "true",
        #"include_24hr_vol": "true",
        #"include_24hr_change": "true",
        "x_cg_demo_api_key": API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    # extract key info
    rows = []
    for coin_id in coins:
        price = None
        market_cap = None
        if isinstance(data, dict) and coin_id in data:
            price = data[coin_id].get("usd")
            market_cap = data[coin_id].get("usd_market_cap")
        rows.append({"id": coin_id, "price": price, "market_cap": market_cap})

    return pd.DataFrame(rows, columns=["id", "price", "market_cap"])

# main
# get list of top 10 coins, then get current pricing in a pandas dataframe
def main():
    print("Top 10 coins by market cap:")
    coins = get_top_coin_list()
    print(coins.head(5).to_string(index=False))

    #generate list of top
    coin_list = []
    for index, row in coins.iterrows():
        coin_list.append(row["id"])

    df = get_current_price(coin_list)
    print(df.head(5).to_string(index=False))

# end main

# call main if file invoked
if __name__ == '__main__':
    main()

# This script calls the CoinGecko API in order to get top coins by market cap and the current price.
# this could be used to compare the different coins by market cap or pricing.
# There are also additional APIs to get historical pricing or daily pricing action OHLC
# This type of data can be used for technical analysis, or rules based trading of coins based on price action
