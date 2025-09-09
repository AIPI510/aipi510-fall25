import requests
import json
import pandas as pd

url = "https://v2.jokeapi.dev/joke/Any"  
params = {
    "amount": 10 
}
response = requests.get(url, params=params)
response.raise_for_status()  

data = response.json()

jokes_list = []
for joke in data.get("jokes", []):
    if joke["type"] == "single":
        jokes_list.append(joke["joke"])
    else:  
        jokes_list.append(f"{joke['setup']} ... {joke['delivery']}")

df = pd.DataFrame(jokes_list, columns=["Joke"])

print(df.head())

#                                                 Joke
# 0  What's Santa's favourite type of music? ... Wrap!
# 1  What did the fish say when it swam into the wa...
# 2  What do you call a caveman's fart? ... A blast...
# 3  Two reasons I don't give money to homeless peo...
# 4  This morning I accidentally made my coffee wit...

###### Annotations
# This script fetches jokes from the JokeAPI and organizes them into a structured format.
# It handles both single-line and two-part jokes, storing them in a pandas DataFrame.
# The first five jokes are displayed for quick preview, making it easy to inspect the data.
