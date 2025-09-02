import requests
import pandas as pd
from bs4 import BeautifulSoup

import requests
import pandas as pd
from bs4 import BeautifulSoup

# Step 1: Define the URL
url = "https://www.basketball-reference.com/leagues/NBA_2024_totals.html"

# Step 2: Get the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find the table by ID
table = soup.find("table", {"id": "totals_stats"})

# Step 4: Read it with pandas
df = pd.read_html(str(table))[0]

# Step 5: Drop rows where Player is "Player" (header rows repeated)
df = df[df["Player"] != "Player"]

# Step 6: Drop rows with missing values
df.dropna(inplace=True)

# Step 7: Reset index
df.reset_index(drop=True, inplace=True)

# Step 8: Print the first 5 rows
print(df.head())

# Step 9: Notes about the data
"""
NOTES:
- This dataset contains total stats for all NBA players in the 2023–2024 season.
- Each row includes player name, age, team, position, cumulative stats and awards won.
- Header rows which are repeated and missing values are removed.
- The first 5 rows are printed, this data can be used for player comparisons, fantasy league projections, or advanced analytics.
"""
