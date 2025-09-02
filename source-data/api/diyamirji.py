#diyamirji.py

import requests
import json
import pandas as pd

url = "https://v2.jokeapi.dev/joke/Spooky"

lst = []
for i in range(10):
    response = requests.get(url)
    data = response.json()
    lst.append([data['setup'], data['delivery'], data['flags']['sexist']])

df = pd.DataFrame(lst)
print(df.head())

# each row of the DataFrame holds the setup of the joke, the delivery of the joke, and whether the joke is sexist
# maybe I can tokenize the setup and the delivery strings into individual words and use the sexist feature as a target value in a ML model
# so if some jokes include certain words that are deemed sexist, the model would be able to predict if a joke will be sexist

