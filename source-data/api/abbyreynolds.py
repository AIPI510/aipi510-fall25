import requests
import pandas as pd

# Get dad jokes from icanhazdadjoke
jokes = []
for _ in range(5):
    r = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    jokes.append(r.json())

# Jokes to DataFrame
df = pd.DataFrame(jokes)[["id", "joke"]]
print(df.head())

"""
NOTES:
- Pulled 5 random dad jokes from icanhazdadjoke.com.
- Each joke has a unique ID and text.
- Could use this for quick entertainment, seeding a jokes app, NLP toy datasets, or just to make
  someone cringe.
"""
