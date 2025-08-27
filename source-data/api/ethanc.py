import requests
import json
import pandas as pd


def run():
    # Get the price data for the top 2000 most popular cryptocurrencies from coinpaprika.com
    response = requests.get("https://api.coinpaprika.com/v1/tickers")

    # Read and process the data into a dataframe
    data = json.loads(response.content.decode())
    df = pd.DataFrame(data)

    # Print the first 5 rows of the dataframe
    print("First 5 Rows of the API Response:")
    print(df.head(5))
    print()

    # Print out some stats about the dataframe
    print("API Response Info:")
    print(df.info())
    print()
    print("Summary:")
    print(df.describe(include='all'))
    print()
    print("Data Types:")
    print(df.dtypes)


if __name__ == "__main__":
    run()


"""
This data can be used to analyze current trends in the crypto market. 

By analyzing values like rank, total supply, and price, we can gain a more comprehensive understanding of popular cryptocurrencies.
Furthermore, values like "beta" can be used to determine the volatility of specific assets.

This data could be used to create charts, inform financial decision making, or educate people on crypto.
"""