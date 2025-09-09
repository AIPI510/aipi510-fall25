import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()  

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.string)

tables = soup.find_all("table", {"class": "wikitable"})  
df = pd.read_html(str(tables[0]))[0]  

df = df.dropna(how="all")  
df = df[~df.iloc[:, 0].str.startswith("Rank")]  

print(df.head())


#   Country/Territory  IMF[1][6]            World Bank[7]            United Nations[8]
#   Country/Territory   Forecast       Year      Estimate       Year          Estimate       Year  
# 0             World  113795678       2025     111326370       2024         100834796       2022  
# 1     United States   30507217       2025      29184890       2024          27720700       2023  
# 2             China   19231705  [n 1]2025      18743803  [n 3]2024          17794782  [n 1]2023  
# 3           Germany    4744804       2025       4659929       2024           4525704       2023  
# 4             India    4187017       2025       3912686       2024           3575778       2023  
#### This data is the nominal GDP ranking of countries around the world. 
# #Can be used to analyze the comparative situation of economic scale in different countries. 
# #For example, studying the GDP distribution of countries across different continents, or identifying the countries with the highest GDP.