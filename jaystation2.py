import requests
import pandas as pd

url = "https://v2.jokeapi.dev/joke/Any?amount=10"  # request 10 jokes
response = requests.get(url)
data = response.json()


jokes_list = []
for joke in data.get("jokes", []):
    if joke["type"] == "single":
        jokes_list.append({
            "category": joke.get("category"),
            "type": "single",
            "joke": joke.get("joke"),
        })
    elif joke["type"] == "twopart":
        jokes_list.append({
            "category": joke.get("category"),
            "type": "twopart",
            "setup": joke.get("setup"),
            "delivery": joke.get("delivery"),
        })


df = pd.DataFrame(jokes_list)


print(df.head())

# notes:
# 1. jokeAPI provides jokes
#this could have multiple uses in multiple websites to show jokes
# . data contains jokes
