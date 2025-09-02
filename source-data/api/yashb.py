import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")



url = "https://api.openweathermap.org/data/2.5/forecast?"
def get_city(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    data = response.json()

    temp_min = []
    temp_max = []
    dt = []
    feels_like = []
    pressure = []

    for i in data["list"]:
        dt.append(i["dt"])
        temp_min.append(i["main"]["temp_min"])
        temp_max.append(i["main"]["temp_max"])
        feels_like.append(i["main"]["feels_like"])
        pressure.append(i["main"]["pressure"])

    df = pd.DataFrame({"DT": dt, "Temp Min": temp_min, "Temp Max": temp_max, "Feels Like": feels_like})
    print(df.iloc[:5])

# Example
print("Weather in Durham\n")
get_city("Durham")

# This data from openweather takes a city as parameter, in this case Durham, and returns a 3 hour interval forcast up to 5 days
# In this, information being stored is datetime, temp min, temp max, feels like, and pressure
# The data can be used to predict future weather, possibly the next upcoming days
