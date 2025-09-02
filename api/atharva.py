import requests
import json
import pandas as pd

URL = "https://api.breakingbadquotes.xyz/v1/quotes/5"

try:
    resp = requests.get(URL, timeout=15)
    resp.raise_for_status()
    data = resp.json()
except requests.RequestException as e:
    raise SystemExit(f"Request failed: {e}")

if not isinstance(data, list):
    raise SystemExit("Unexpected response format")

rows = [{"quote": d.get("quote"), "author": d.get("author")} for d in data]
df = pd.DataFrame(rows)

print(df.head())

"""
Data source: Breaking Bad Quotes API... https://api.breakingbadquotes.xyz/
Returns random quotes and the speaker... author.
Possible uses:
- Use when wanting some inspiration or random deep thoughts to ponder over
- Use if you want to feel cool
- Use when discussing Breaking Bad with your other cool friends and wanting to pull up random quotes
"""
