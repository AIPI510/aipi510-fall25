import requests

from bs4 import BeautifulSoup

import pandas as pd

html_data = requests.get("https://www.timeanddate.com/holidays/us/")

df = pd.read_html(str(html_data.text))

print(df)

"""
Notes: My data consists US holiday dates along with states that observe them on the corresponding 
days. I would use this data to create a general information web applications about various US holiday
dates along with the US dtates that observe them.
"""