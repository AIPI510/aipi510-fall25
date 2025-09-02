import requests
import json
import pandas as pd

API_KEY = 'affa4f93a0cbf32b36ea6a33e34ce132'

def forecast(city):
    """
    This function takes an city name as input, then uses the Open Weather API to 
    retrieve timestamped forecast of temp, humidity, and description 
    """

    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": API_KEY, # API key defined above
        "units": "metric"  # temperature in Celsius
    }

    response = requests.get(url, params=params)
    data = response.json()

    forecast = data["list"]

    df = pd.DataFrame(columns=["datetime", "temp", "humidity", "description"]) # creating empty DF

    for hour in forecast:
        weather = {
            "datetime" : hour["dt_txt"],
            "humidity" : hour["main"]["humidity"],
            "temp" : hour["main"]["temp"],
            "description" : hour["weather"][0]["description"]
        }
        df = pd.concat([df, pd.DataFrame([weather])], ignore_index=True)

    return df

city = "Nashville"

print(forecast(city).head(5))

"""
The data provided by this function is 3 hour forecast for the next 4 days that includes datetime, temp, humidity, description
This data could be used to train a model that predicts temperature by time of day or predicts humidity from temp, datetime, and description
A predictive weather model can be useful for manyh things from commidity trading to navigation
As a summary, data is given in 3 hour increments and is stored in this order datetime, temp, humidity, description
"""