import requests
from bs4 import BeautifulSoup
import pandas as pd 


response = requests.get("https://www.basketball-reference.com/leagues/NBA_2024_totals.html")
# Parse the HTML content
Soup_output = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the data
# id means "identifier" and totals_stats is the identifier for the total statistics table
table = Soup_output.find('table', {'id': 'totals_stats'})
 #The above code snippet was generated using chatgpt 5  on 9/2/25 at 1:05pm and then modified slightly to change labels



# extract the data into a pandas DataFrame
# we use the read_html function from pandas to read the HTML table directly into a DataFrame
# str(table) converts the BeautifulSoup table object into a string representation because it allows pandas to parse the HTML
# [0] is used to select the first table found (in case there are multiple tables .. assuming first table is the one we want)
df = pd.read_html(str(table))[0]


##  Clean data

# drop rows with missing values or headers repeated in the table)
df = df.dropna()

# Remove the header row that was included in the table
df = df[df['Rk'] != 'Rk']

#The above code snippet was generated using chatgpt 5 on 9/2/25 at 1:15pm and then modified slightly to change labels

# Reset the index
df = df.reset_index(drop=True)

# print the first 5 rows
print(df.head())

# Describe data and how it can be used
"""
The dataset contains player statistics for the 2024 NBA season, including key metrics such as points, rebounds, assists, and more. 
This data can be used for various analyses, including player performance evaluation, 
team strategy development, and fantasy basketball insights.

"""

# data result:

"""
  df = pd.read_html(str(table))[0]
    Rk                   Player   Age Team Pos     G    GS      MP  ...    AST    STL   BLK    TOV     PF     PTS  Trp-Dbl                        Awards
0  1.0              Luka Dončić  24.0  DAL  PG  70.0  70.0  2624.0  ...  686.0   99.0  38.0  282.0  149.0  2370.0     21.0          MVP-3,CPOY-6,AS,NBA1
1  2.0  Shai Gilgeous-Alexander  25.0  OKC  PG  75.0  75.0  2553.0  ...  465.0  150.0  67.0  162.0  184.0  2254.0      0.0   MVP-2,DPOY-7,CPOY-3,AS,NBA1
2  3.0    Giannis Antetokounmpo  29.0  MIL  PF  73.0  73.0  2567.0  ...  476.0   87.0  79.0  250.0  210.0  2222.0     10.0  MVP-4,DPOY-9,CPOY-12,AS,NBA1
3  4.0            Jalen Brunson  27.0  NYK  PG  77.0  77.0  2726.0  ...  519.0   70.0  13.0  186.0  144.0  2212.0      0.0          MVP-5,CPOY-5,AS,NBA2
4  5.0             Nikola Jokić  28.0  DEN   C  79.0  79.0  2737.0  ...  708.0  108.0  68.0  237.0  194.0  2085.0     25.0          MVP-1,CPOY-4,AS,NBA1

[5 rows x 32 columns]

"""