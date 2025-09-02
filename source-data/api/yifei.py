import requests
import json
import pandas as pd


def fetch_jokes(amount=20, categories="Any"):
    base_url = f"https://v2.jokeapi.dev/joke/{categories}"

    params = {"amount": amount}

    # 1) Make an HTTP GET request
    resp = requests.get(base_url, params=params, timeout=10)
    resp.raise_for_status()

    # 2) Parse JSON response
    payload = resp.json()

    # JokeAPI returns either a single object or {"jokes": [...]}
    jokes_raw = payload["jokes"] if isinstance(payload, dict) and "jokes" in payload else [payload]

    # 3) Stores relevant fields into a DataFrame
    rows = []
    for j in jokes_raw:
        if j.get("error"):
            continue

        row = {
            "id": j.get("id"),
            "category": j.get("category"),
            "type": j.get("type"),               # 'single' or 'twopart'
            "joke_text": j.get("joke") if j.get("type") == "single" else f"{j.get('setup')} || {j.get('delivery')}",
            "safe": j.get("safe"),
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    return df


if __name__ == "__main__":
    # Fetch 20 safe jokes across all categories
    df = fetch_jokes(
        amount=20,
        categories="Any",
    )

    # Print the first 5 rows
    print(df.head())

    """
    Notes:
    - Source: JokeAPI v2, retrieved via an HTTP GET request.
    - Each row is a joke. 'joke_text' unifies 'single' and 'twopart' formats for downstream use.
    - Repro: requires 'requests' and 'pandas'. Run with: `python api/yifei_week2.py`.
    """    