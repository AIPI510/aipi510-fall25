import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

# Gummy bear wiki page
url = "https://en.wikipedia.org/wiki/Gummy_bear"

# Fetch HTML with user agent to avoid 503 errors
r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0 (Macintosh) AppleWebKit/537.36 Chrome/120 Safari/537.36"},
    timeout=20,
)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")

# Find wikitable
table = soup.find("table")

# To df (needed to use StringIO to satisfy SoupStrainer requirements)
df = pd.read_html(StringIO(str(table)))[0]

# Light clean
df = df.dropna(how="all").reset_index(drop=True)

print(df.head())

"""
NOTES:
- Sourced the Gummy Bear wiki page with user agent.
- Pulled the first wikitable from Wikipedia's Gummy Bear page.
- Droped empty columns.
- Script shows gummy bear-related data (yummy).
- Could be useful for quick data exploration if you are curious about candy.
"""
