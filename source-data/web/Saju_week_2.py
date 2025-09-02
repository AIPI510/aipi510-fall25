import requests
from bs4 import BeautifulSoup
import pandas as pd

#5. Use requests.get(url) to download HTML from your selected page.
#6. Use BeautifulSoup to find the desired <table> and parse it into a DataFrame.
#7. Clean the data (e.g., drop rows with missing values or headers repeated in the table).
#8. Print the first 5 rows.
#9. Add 3–5 lines of notes at the bottom of the script describing your data and how you might use it.
#10. Commit

url = "https://www.scrapethissite.com/pages/forms/"

#Make the request
response = requests.get(url)
#print(response)

soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

tables = soup.find_all("table")
#print(f"Found {len(tables)} tables.")
#print(tables)
print(tables)



#I used GitHub CoPilot top help me use Beatiful Soup to get the data from this website 
#and to get the tables but I could not figure out how to get the module to get the tables.
