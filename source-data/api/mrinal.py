# import

import requests
import json
import pandas as pd

response = requests.get("https://v2.jokeapi.dev/joke/Programming,Christmas?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single&amount=10")
data = json.loads(response.text)
# get the jokes dict
df = pd.json_normalize(data["jokes"])
print(f"Safe and Unsafe jokes - {df.shape}")
df_safe = df[df["safe"]]
print(f"Safe and Unsafe jokes - {df_safe.shape}")
print(df_safe.head())

"""
My data is "SAFE" programming jokes. I would use this to create a bag of words that my fellow programmers would find funny.
"""