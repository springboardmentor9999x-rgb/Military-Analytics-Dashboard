import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import re

def get_data_from_url(url):
    """Visits a page and extracts {Country: Value} pairs."""
    data = []
    try:
        # 1. Fetch page
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(page.content, 'html.parser')

        # 2. Find all country rows (Using the specific class names)
        rows = soup.select("div.recordsetContainer")

        for row in rows:
            country = row.select_one("span.textShadow").text.strip()
            # The value is usually the last 'textLarge' item in the row
            raw_val = row.select("span.textLarge")[-1].text.strip()
            
            # 3. Clean the number (remove commas like '1,200' -> '1200')
            clean_val = re.search(r"-?\d+\.?\d*", raw_val.replace(",", ""))
            if clean_val:
                data.append({'Country': country, 'Value': float(clean_val.group())})
                
    except Exception as e:
        print(f"  Error: {e}")
    
    return pd.DataFrame(data)

# --- MAIN PROGRAM ---

print("Starting Scraper...")
final_df = pd.DataFrame()

# 1. Read the text file (Filtering only lines with arrows)
with open('links_for_military_data.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if '→' in line]

# 2. Loop through each link
for line in lines:
    # Split "URL → Column_Name"
    url, col_name = line.split('→')
    url = url.strip().replace('- ', '') # Clean URL
    col_name = col_name.strip()          # Clean Column Name
    
    print(f"Scraping: {col_name}")
    
    # Fetch data
    temp_df = get_data_from_url(url)
    
    if not temp_df.empty:
        # Rename generic 'Value' to the specific column name (e.g., 'total_tanks')
        temp_df.rename(columns={'Value': col_name}, inplace=True)
        
        # Merge into the master list
        if final_df.empty:
            final_df = temp_df
        else:
            final_df = pd.merge(final_df, temp_df, on='Country', how='outer')
            
    time.sleep(1) # Pause specifically to avoid getting blocked

# 3. Save to CSV
final_df.sort_values('Country').to_csv('military_raw_data.csv', index=False)
print("Success! Data saved to military_raw_data.csv")