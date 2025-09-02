import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Add more comprehensive headers to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

def scrape_nba_stats(year=2024):
    """
    Scrape NBA player statistics for a given year
    """
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_totals.html"
    
    try:
        # Add a small delay 
        time.sleep(1)
        
        # Create a session for better connection handling
        session = requests.Session()
        session.headers.update(headers)
        
        # Make request
        print(f"Fetching data from: {url}")
        response = session.get(url, timeout=10)
        response.raise_for_status()
        
        print(f"Response status code: {response.status_code}")
        print(f"Response content type: {response.headers.get('content-type', '')}")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        page_text = soup.get_text().lower()
        if any(indicator in page_text for indicator in ['cloudflare', 'please enable javascript', 'access denied', 'blocked']):
            print("Warning: Page might be blocked or requires JavaScript")
            return None
        
        # Basketball Reference uses 'totals_stats' for the table ID
        table = soup.find('table', {'id': 'totals_stats'})
        
        if not table:
            print("No tables found on the page")
            return None

        if table:
            print("Table found successfully!")
            
            try:
                # Use pandas read_html directly on the URL
                print("Trying pandas read_html method...")
                dfs = pd.read_html(url, header=1, requests_kwargs={'headers': headers})  # header=1 to skip the first row if it's not proper headers
                
                if dfs:
                    df = dfs[0]  # Usually the first table is what we want
                    print("DataFrame created successfully using pd.read_html!")
                else:
                    raise ValueError("No tables found by pd.read_html")
                    
            except Exception as e:
                print(f"pd.read_html failed: {e}")
                print("Trying manual table parsing...")
                
                #  Manual parsing
                try:
                    # Find header row
                    header_row = table.find('thead')
                    if header_row:
                        column_headers = [th.get_text().strip() for th in header_row.find_all('th')]
                    else:
                        # Fallback: use first row as headers
                        first_row = table.find('tr')
                        column_headers = [th.get_text().strip() for th in first_row.find_all(['th', 'td'])]
                    
                    # Find data rows
                    tbody = table.find('tbody')
                    if tbody:
                        rows = tbody.find_all('tr')
                    else:
                        rows = table.find_all('tr')[1:]  # Skip header row
                    
                    # Extract data
                    data = []
                    for row in rows:
                        # Skip rows that are just headers (common in basketball-reference)
                        if row.get('class') and 'thead' in ' '.join(row.get('class')):
                            continue
                            
                        cells = row.find_all(['td', 'th'])
                        if cells:
                            row_data = [cell.get_text().strip() for cell in cells]
                            data.append(row_data)
                    
                    # Create DataFrame
                    df = pd.DataFrame(data, columns=column_headers[:len(data[0])] if data else column_headers)
                    print("DataFrame created successfully using manual parsing!")
                    
                except Exception as manual_error:
                    print(f"Manual parsing also failed: {manual_error}")
                    return None
            
            # Clean the DataFrame
            if not df.empty:
                # Remove any completely empty rows
                df = df.dropna(how='all')
                
                # Basketball Reference sometimes has repeated header rows, remove them
                df = df[df.iloc[:, 0] != 'Player']  
                
                # Reset index
                df = df.reset_index(drop=True)
                
                print(f"\nDataFrame shape: {df.shape}")
                print(f"Columns: {list(df.columns)}")
                print("\nFirst 5 rows:")
                print(df.head())
                
                return df
            else:
                print("DataFrame is empty")
                return None
        
        else:
            print("No suitable table found")
            return None
            
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

if __name__ == "__main__":
    df = scrape_nba_stats(2024)
    
    if df is not None:
        print("\n" + "="*50)
        print("SUCCESS! Data scraped successfully")
        print("="*50)
        
    else:
        print("\n" + "="*50)
        print("FAILED! Could not scrape data")
        print("="*50)

# This code has been mostly generated by Claude (Tried doing it myself first, but got an error with reading the table and didn't know how to manually parse it properly). 
# But anyway, this script is a basketball table with player data from the 2023 - 2024 season. It could be helpful to predict games using it as historical data, predict player stats,
#or just use the stats to analyze player performance. 

