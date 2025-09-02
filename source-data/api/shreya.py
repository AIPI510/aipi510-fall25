import requests
import json
import pandas as pd
import os

response=requests.get("https://v2.jokeapi.dev/joke/Programming?amount=25")
#pulling the data from the API
data=response.json()
df= pd.json_normalize(data)
#normalizing the data to create a dataframe
df=df.explode("jokes").reset_index(drop=True)
print(df.head(5))