import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.worldometers.info/gdp/gdp-by-country/"

# 5) Download HTML
resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
resp.raise_for_status()
html = resp.text

# 6) Find the target table and parse into a DataFrame
soup = BeautifulSoup(html, "html.parser")
table = soup.select_one("table#example2") or soup.select_one("table.table")

if table is None:
    raise RuntimeError("Target table not found on Worldometer page.")

df = pd.read_html(str(table))[0]  # parse the found table into DataFrame

# 7) Light cleaning
df.columns = [c.strip() for c in df.columns]  # normalize column names

# Identify columns we care about
country_col = next((c for c in df.columns if "Country" in c), None)
rank_col = "#" if "#" in df.columns else next((c for c in df.columns if "Rank" in c), None)
gdp_col = next((c for c in df.columns if "GDP" in c and "nominal" in c), None)
if gdp_col is None:
    gdp_col = next((c for c in df.columns if c.startswith("GDP")), None)

# Coerce GDP to numeric (remove $, commas, spaces)
if gdp_col:
    df[gdp_col] = (
        df[gdp_col].astype(str).str.replace(r"[^\d.\-]", "", regex=True).replace({"": pd.NA})
    )
    df[gdp_col] = pd.to_numeric(df[gdp_col], errors="coerce")

# Keep a minimal tidy subset if present
keep = [c for c in [rank_col, country_col, gdp_col] if c]
df = df[keep] if keep else df
df = df.rename(columns={rank_col: "Rank", country_col: "Country", gdp_col: "GDP_nominal_USD"})
df = df.dropna(subset=["Country"]).reset_index(drop=True)

# 7) Print the first 5 rows
print(df.head())

# Optional: save a CSV for convenience
df.to_csv("data_gdp_worldometers.csv", index=False)

"""
Notes:
- Source: Worldometer 'GDP by Country (nominal)'.
- Tools: requests to fetch HTML; BeautifulSoup to locate the main table; pandas.read_html to parse.
- Cleaning: stripped citation/symbols from column values; coerced GDP to numeric; kept Rank/Country/GDP.
- Use cases: quick ranking/visualization; join with population to get GDP per capita.
"""
