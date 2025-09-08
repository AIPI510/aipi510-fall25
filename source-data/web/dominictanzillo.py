import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://dominictanzillo.github.io", verify=False)
soup = BeautifulSoup(response.content, "html.parser")

experience_section = soup.find("section", {"id": "experience"})

# Grab all experience cards
experience_cards = experience_section.find_all("div", class_="card")

records = []
for card in experience_cards:
    title = card.find("h4", class_="exp-title").get_text(strip=True)
    company = card.find("h4", class_="exp-company").get_text(strip=True)
    dates = card.find("div", class_="exp-meta").get_text(" ", strip=True)
    description = " ".join(li.get_text(strip=True) for li in card.find_all("li"))

    records.append({
        "Title": title,
        "Company": company,
        "Dates": dates,
        "Description": description
    })

# Convert to DataFrame
df = pd.DataFrame(records)
print(df)\

### Output

### From my own personal website I scraped the various columns and subheadings and then outputed them into a table that I made. Somewhat cumbersome but in this case I scarpped and then separated the data from the webpage. IT is curious that I had to turn on false for the safety checks for the get request. I might uninstall python and reinstall via homebrew in the future.
#                                    Title  ...                                        Description
#0                      Software Developer  ...  Working on a variety of NASA, Air Force, and h...
#1                    Volunteer Researcher  ...  Shadowed hyperbaric physicians and critical ca...
#2  Undergraduate Space Research Associate  ...  Built machine learning models to predict USAF ...
#3                Undergraduate Researcher  ...  Investigated error rate in medical software us...
#
#[4 rows x 4 columns]
#
#Process finished with exit code 0