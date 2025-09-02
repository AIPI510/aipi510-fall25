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

# I used GitHub co pilot to help me get to the week 2 branch and give me the syntax for getting to week 2. 09/2/2025.