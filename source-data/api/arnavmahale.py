import requests
import json
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
  params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
  }

  response = requests.get(API_URL, params=params)

  if response.status_code != 200:
    print(f"Error: Unable to fetch weather for {city}.")

  data = response.json()

  return {
        "city": data["name"],
        "temp_c": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }


if __name__ == "__main__":
  cities = ["Durham", "Raleigh", "Boston", "New York", "San Francisco"]
  rows = []
  for city in cities:
    weather = get_weather(city)
    if weather:
      rows.append(weather)
    
  df = pd.DataFrame(rows)
  print(df.head())


###################################
# This script gets weather data for the cities: Durham, Raleigh, Boston, New York, San Francisco
# It provides the temperature, humidity, and current state of the clouds of the cities. It can be
# used to compare weather across cities and create a dashboard. Could be extended for logging
# daily weather changes over time.
###################################