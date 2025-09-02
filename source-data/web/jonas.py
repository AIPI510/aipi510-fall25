import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://arxiv.org/list/cs.AI/recent")
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('div', class_='list-title mathjax')

# first 5 titles with authors
for article in articles[:5]:
    title = article.get_text(strip=True)
    print(f"Title: {title}")
    authors = article.find_next('div', class_='list-authors').get_text(strip=True)
    print(f"Authors: {authors}")

# This is getting 5 articles from the cs.AI category on arXiv
# Could be used for keeping on top of the most recent developments in AI research
# Potentially useful for  users that want to be on top of recent papers.