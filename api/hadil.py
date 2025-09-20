import requests
import json
import pandas as pd

API_URL = "https://v2.jokeapi.dev/joke/Any"
PARAMS = {"amount": 20, "safe-mode": ""}

def fetch_jokes():
    resp = requests.get(API_URL, params=PARAMS, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    jokes = data.get("jokes") or [data]
    rows = []
    for j in jokes:
        if j.get("type") == "single":
            rows.append({
                "category": j.get("category"),
                "type": j.get("type"),
                "joke": j.get("joke"),
                "setup": None, "delivery": None,
                "safe": j.get("safe"), "id": j.get("id"), "lang": j.get("lang")
            })
        else:
            rows.append({
                "category": j.get("category"),
                "type": j.get("type"),
                "joke": None,
                "setup": j.get("setup"),
                "delivery": j.get("delivery"),
                "safe": j.get("safe"), "id": j.get("id"), "lang": j.get("lang")
            })
    df = pd.DataFrame(rows).drop_duplicates().dropna(how="all")
    print("JokeAPI — first 5 rows:")
    print(df.head())
    return df

if __name__ == "__main__":
    df = fetch_jokes()
    notes = """
NOTES:
- Source: JokeAPI v2 (no key). Pulled 20 safe-mode jokes.
- Fields: category, type (single/twopart), text (joke OR setup/delivery), metadata.
- Uses: sentiment/length analysis, topic clustering, style prompts.
- Caveats: occasional repeats; rate limits; safe-mode filters edgy content.
"""
    print(notes)

