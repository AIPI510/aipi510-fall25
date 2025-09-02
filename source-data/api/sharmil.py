import requests
import pandas as pd
import json

# 1. API endpoint
url = "https://v2.jokeapi.dev/joke/Any"

# 2. List to store jokes
jokes = []

# 3. Fetch 5 jokes
for i in range(5):
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = json.loads(response.text)
        
        if joke_data["type"] == "single":
            joke_text = joke_data["joke"]
        else:  # "twopart"
            joke_text = f"{joke_data['setup']} ... {joke_data['delivery']}"

        jokes.append({
            "Category": joke_data["category"],
            "Joke": joke_text
        })
    else:
        print(f"Error fetching joke {i+1}: {response.status_code}")

# 4. Store in DataFrame
df = pd.DataFrame(jokes)

# 5. Print first 5 rows
print(df.head())

# 6. Notes
"""
NOTES:
- This script uses the JokeAPI (https://v2.jokeapi.dev) to fetch 5 random jokes.
- Each joke can be a 'single' one-liner or a 'twopart' joke (setup + punchline).
- The data is stored in a pandas DataFrame and can be exported, filtered, or visualized for fun.
- JokeAPI requires no API key, and is great for demo/testing JSON API calls.
- Portions of this script were generated using OpenAI's ChatGPT (GPT-4) to assist with API integration, data parsing, and Python scripting.
"""
