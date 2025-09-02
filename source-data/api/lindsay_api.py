import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv

# Select openweathermap API
# I will be using the open weather map API
# read the documentation from the API
# The API documentation can be found at: https://openweathermap.org/api

# Load environment 
load_dotenv()

# Get the API Key from the .env
openweather_api_key = os.getenv("openweather_api_key")


#make a GET request
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={openweather_api_key}")
weather_data = response.json()

# Convert the JSON data to a pandas DataFrame
df = pd.json_normalize(weather_data)

# parse the JSON response
parsed_weather_info = {
    "city": df["name"].values[0],
    "temperature": df["main.temp"].values[0],
    "weather": df["weather"].values[0][0]["description"]
}
# The above code snippet was generated using Chat GPT on 9/2/25 at 1:31pm and then modified in order to change the labels and to delete humidity.


# Display the weather information
# print first 5 rows of data frame
print(df.head())
# 3-5 lines of code describing the data and possible uses:
""" 
The DataFrame contains weather information for a specific city,
including temperature and weather.
This data can be used for reporting and users interested in seeing the weather forecast.
"""

print(parsed_weather_info)

#outputed data:

"""
                                             weather      base  visibility          dt  timezone  ...  sys.type   sys.id  sys.country  sys.sunrise  sys.sunset
0  [{'id': 803, 'main': 'Clouds', 'description': ...  stations       10000  1756834756      3600  ...         2  2075535           GB   1756790098  1756838749

[1 rows x 27 columns]
{'city': 'London', 'temperature': 291.08, 'weather': 'broken clouds'}

"""