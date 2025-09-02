import requests
import json
import pandas as pd

#URL
url = "https://v2.jokeapi.dev/joke/Any?format=json"

#Make the request
response = requests.get(url)

#Parse JSON
data = response.json()

print(data)