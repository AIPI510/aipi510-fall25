import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://arxiv.org/list/cs.AI/recent")
soup = BeautifulSoup(response.text, 'html.parser')

data = []
dts = soup.find_all('dt')[:10]

for dt in dts:
    a_tag = dt.find('a', title='Abstract')
    if a_tag:
        arxiv_id = a_tag.text.strip()
        link = 'https://arxiv.org' + a_tag['href']
        
        dd = dt.find_next_sibling('dd')
        if dd:
            title_span = dd.find('span', class_='descriptor', string='Title:')
            title = title_span.next_sibling.strip() if title_span else 'N/A'
            
            authors_div = dd.find('div', class_='list-authors')
            authors = authors_div.get_text(strip=True).replace('Authors: ', '') if authors_div else 'N/A'
            
            data.append({'arxiv_id': arxiv_id, 'title': title, 'authors': authors, 'link': link})

df = pd.DataFrame(data)
df = df.dropna(subset=['title'])
print(df[['arxiv_id', 'title']].head(5))

# Scrapes recent cs.AI papers from arXiv: arXiv ID, title, authors, link.
# Cleans incomplete rows via dropna.
# I'd use it to curate AI paper summaries, e.g., scan titles/authors for LLM trends.