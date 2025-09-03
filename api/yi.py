import requests
import json
import pandas as pd

def fetch_medicaid_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data: {response.status_code}")
    # Parse response and then store in a dataframe
    data = response.json().get('results')
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    # URL for Medicaid data API
    url = "https://data.medicaid.gov/api/1/datastore/query/e85033c7-367e-467e-9e81-8e85048102b8/0?limit=10"
    
    # Fetch the data
    df = fetch_medicaid_data(url)
    
    # Print first 5 rows
    print("First 5 rows of Medicaid data:")
    print(df.head())

    # This is the 2023 Child and Adult Health Care Quality Measures data
    # It contains various health care quality metrics for Medicaid and CHIP programs across different states.
    # it can be used for analysis of health care quality and performance across states.