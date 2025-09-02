import json 
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

NASA_KEY = os.getenv('NASA_KEY')

base_url=f"https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={NASA_KEY}"


response = requests.get(base_url)
data = json.loads(response.text)

df = pd.DataFrame(data['near_earth_objects'])
print("Dataframe:", df[:10])
print("INFO:", df.info())
print("DESCRIPTION:", df.describe())


neo0 = pd.DataFrame(df['close_approach_data'][0])
neo1 = pd.DataFrame(df['orbital_data'][0])
neo0.to_csv('alex_close_approach_data.csv')
print(neo0, neo1)

# I could use near orbit data to learn more about future orbits and trajectory through mathematics.
