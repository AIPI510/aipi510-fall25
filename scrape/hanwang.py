import requests
from bs4 import BeautifulSoup
import pandas as pd

# Find a beautiful soup caption by caption name
def find_table_by_caption(soup, target_caption):
    found_table = None

    for caption in soup.find_all('caption'):
        if caption.get_text(strip=True) == target_caption:
            found_table = caption.find_parent('table')
            break
    return found_table

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

# get the target URL, add user-agent header otherwise might get 403 error; Make soup
response = requests.get(url, headers=headers)
response.raise_for_status() #make sure no error / 200
soup = BeautifulSoup(response.content, features="lxml")

# find specific table on page using the caption
caption = "GDP forecast or estimate (million US$) by country"
table = find_table_by_caption(soup, caption)
#print(table)

# remove superscript to clean data
superscripts = table.find_all('sup')
for sup_tag in superscripts:
    sup_tag.decompose()

#pick the first table found and convert to pandas dataframe
df = pd.read_html(str(table))[0]

#un-span the columns, and cleanup names
df.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col
              for col in df.columns.values]
df.rename(columns={'Country/Territory_Country/Territory': 'Country/Territory'}, inplace=True)

print(df.head(5).to_string(index=False))
# Should have these columns:
# Country/Territory IMF_Forecast IMF_Year World Bank_Estimate World Bank_Year United Nations_Estimate United Nations_Year


# The table is a list of country/territory and its GDP for different years, baed on different sources
# It can be used to compare the size of the economy (with GDP as proxy) with each other.
# The GDP can also be combined with other data facts for unit comparisons
# (i.e. GDP per sq-mile, GDP per population, etc..)

