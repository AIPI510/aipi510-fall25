import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    data = []
    tables = soup.find_all('table', {'class': 'wikitable'})
    if not tables:
        raise ValueError("No tables found on the page.")
    table = tables[0]
    
    # Extract headers
    header_rows = table.find_all("tr")[:2]

    # First row with padding for colspan 2
    top_headers = []
    for th in header_rows[0].find_all("th"):
        colspan = int(th.get("colspan", 1))
        text = th.get_text(strip=True)
        top_headers.extend([text] * colspan)

    # Second row
    sub_headers = [th.get_text(strip=True) for th in header_rows[1].find_all("th")]

    # If lengths differ, pad
    if len(top_headers) > len(sub_headers):
        sub_headers = [""] * (len(top_headers) - len(sub_headers)) + sub_headers

    # Combine
    headers = [
        f"{top} {sub}".strip()
        for top, sub in zip(top_headers, sub_headers)
    ]
        
    # Extract data rows
    for row in table.find_all('tr')[2:]:
        cells = row.find_all('td')
        if cells:
            values = [cell.get_text(strip=True) for cell in cells]
            if len(values) == len(headers) and values[0]:
                data.append(values)
    df = pd.DataFrame(data, columns=headers)
    
    return df

if __name__ == "__main__":
    # URL for GDP data from Wikipedia
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
    
    # Scrape the data
    df = scrape_data(url)
    
    # Print first 5 rows
    print("First 5 rows of GDP data:")
    print(df.head())
    
    # Data description and potential uses:
    # This dataset lists GDP forecasts and estimates for each country from the IMF, World Bank, and United Nations.
    # It can be used for things like comparing economies, studying growth trends, 
    # creating charts or dashboards, or even building simple forecasting models.