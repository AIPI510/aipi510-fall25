import requests
import json
import pandas as pd

# Chosen API: JokeAPI

# Make a GET request
response = requests.get("https://v2.jokeapi.dev/joke/Any")
raw_data = response.json()

# Parse the JSON response
joke = raw_data["joke"]
flag = raw_data["flags"]
safe = raw_data["safe"]
lang = raw_data["lang"]

# Store relevant fields into a DataFrame
data_df = pd.DataFrame([joke, flag, safe, lang])

# Print the first 5 rows of the DataFrame
print(data_df.head())

"""
Notes: The data stored in the DataFrame include a random joke, flags indicating whether the joke is nsfw, religious, political, 
racist, sexist, and explicit, whether the joke is safe, and the joke's language. The possible uses of this data includes generating 
random jokes for entertainment purposes or third-party applications and understanding and informing others of potential concerns 
regarding the appropriateness of such jokes in terms of their content.
"""