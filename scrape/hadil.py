import requests
from bs4 import BeautifulSoup
import pandas as pd

# Pretend to be a browser so sites don't 403-block us
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

NBA_URL = "https://www.basketball-reference.com/leagues/NBA_2024_totals.html"
WIKI_URL = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

def scrape_nba_totals_bs():
    resp = requests.get(NBA_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    table = soup.find("table", {"id": "totals_stats"})
    if table is None:
        raise RuntimeError("Could not find table id='totals_stats'")

    header = [th.get_text(strip=True) for th in table.thead.find_all("th")]
    rows = []
    for tr in table.tbody.find_all("tr"):
        if "class" in tr.attrs and "thead" in tr["class"]:
            continue
        cells = [td.get_text(strip=True) for td in tr.find_all(["th", "td"])]
        if len(cells) == len(header):
            rows.append(cells)

    df = pd.DataFrame(rows, columns=header)
    df = df[df["Player"].ne("") & df["Player"].ne("Player")]
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")
    df = df.dropna(axis=1, how="all")
    print("NBA Totals — first 5 rows:")
    print(df.head())
    return df

def scrape_wiki_gdp_readhtml():
    resp = requests.get(WIKI_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    # read_html can take raw HTML to avoid its own fetch without headers
    tables = pd.read_html(resp.text, flavor="bs4")

    df = None
    for t in tables:
        lower = [str(c).lower() for c in t.columns]
        if any(("country" in c or "territory" in c) for c in lower):
            df = t
            break
    if df is None:
        raise RuntimeError("Could not find GDP-by-country table")
    df = df.dropna(how="all")
    first_col = df.columns[0]
    df = df[df[first_col].astype(str).str.lower() != "country"]
    df.columns = [str(c).strip().replace("\n", " ") for c in df.columns]
    for col in df.columns:
        if "gdp" in str(col).lower():
            df[col] = (
                df[col].astype(str)
                .str.replace(r"[^\d\.\-]", "", regex=True)
                .replace({"": None})
            )
            df[col] = pd.to_numeric(df[col], errors="coerce")

    print("Wikipedia GDP (nominal) — first 5 rows:")
    print(df.head())
    return df

if __name__ == "__main__":
    print("Starting scraper...")
    try:
        df = scrape_nba_totals_bs()
    except Exception as e:
        print("Error while scraping NBA site:", e)
        print("Switching to Wikipedia GDP scrape instead...")
        df = scrape_wiki_gdp_readhtml()

    print("Done! First 5 rows above.")
    notes = """
NOTES:
- Source: Basketball-Reference (NBA 2024 totals) OR Wikipedia (nominal GDP).
- I set a browser-like User-Agent header to avoid 403 blocks.
- Cleaned repeated header rows and coerced numeric-looking columns.
- Uses: simple EDA (leaders/totals) or GDP joins (e.g., with population).
- Caveat: page structure changes can break scrapers.
"""
    print(notes)
