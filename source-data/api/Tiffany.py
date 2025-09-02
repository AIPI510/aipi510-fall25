import requests
import json
import pandas as pd

url="https://v2.jokeapi.dev/joke/Programming"
response = requests.get(url)
data = response.json()
dictionary={
    "joke": data.get("joke")
}
df=pd.DataFrame([dictionary])

print(df)