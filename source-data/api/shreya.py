import requests
import json
import pandas as pd
import os

response=requests.get("https://v2.jokeapi.dev/joke/Programming?amount=25")
#pulling the data from the API
data=response.json()
df= pd.json_normalize(data)
#normalizing the data to create a dataframe
df["jokes"]=df.apply(lambda row: [row["setup"] + " " + row["delivery"]] if row["type"]=="twopart" else [row["joke"]], axis=1)
#combining the setup and delivery columns for two-part jokes, and keeping the joke column for single-part jokes
# df=df.explode("jokes").reset_index(drop=True)
print(df.head(5))