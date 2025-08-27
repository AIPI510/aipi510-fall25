import requests
import json
import pandas as pd


def run():
    # Get the list of largest companies in the United States by revenue by reading the wikipedia page
    response = requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue",
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"})

    # Read and process the html
    tables = pd.read_html(response.text)
    
    # Full table is the second table on the webpage
    df = tables[1]

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

    # Data types
    print("Data Types:")
    print(df.dtypes)


if __name__ == "__main__":
    run()


"""
This data can be used to analyze the largest companies in the United States by revenue. 

By looking at values like rank, revenue, and total equity, we can gain a better understanding of top performing companies and how they compare to one another.
This data could be used to create charts, and understand current economic trends.
"""