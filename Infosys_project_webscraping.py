# --------------------------------------------------
# Contributor: Deepak Avachitkar
# Project: Military Analytics Dashboard
# --------------------------------------------------

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# User-Agent header to avoid basic blocking
HEADERS = {"User-Agent": "Mozilla/5.0"}


# Function: read_links_txt
# Reads metric URLs from a TXT file
# Cleans bullets/arrows and returns valid URLs

def read_links_txt(path):
    links = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            # Remove bullets and arrow symbols if present
            line = line.replace("- ", "")
            if "→" in line:
                line = line.split("→")[0].strip()

            # Keep only valid URLs
            if line.startswith("http"):
                links.append(line)

    return links



# Function: scrape_global_firepower_data
# 1. Scrapes base country ranking data
# 2. Scrapes multiple metric pages from TXT file
# 3. Merges all metrics country-wise
# 4. Cleans numeric values
# .............................................................
def scrape_global_firepower_data():

    # Base page containing country ranks
    base_url = "https://www.globalfirepower.com/countries-listing.php"

    # TXT file containing metric URLs
    links_file = r"C:\Users\avach\links_for_military_data.txt"
    metric_urls = read_links_txt(links_file)

    # ................ Scrape base ranking data ...............
    r = requests.get(base_url, headers=HEADERS, timeout=30)
    soup = BeautifulSoup(r.text, "html.parser")

    containers = soup.find_all(
        "div", class_="picTrans recordsetContainer boxShadow zoom"
    )

    ranks, countries = [], []

    for item in containers:
        try:
            # Extract world rank
            ranks.append(
                item.find("span", class_="textWhite textLarge textBold").text.strip()
            )
            # Extract country name
            countries.append(
                item.find("span", class_="textWhite textLarge textShadow").text.strip()
            )
        except:
            continue

    # Base DataFrame with rank and country
    df_main = pd.DataFrame({"rank": ranks, "country": countries})

    # ............. Scrape metric pages ...........
    for url in metric_urls:

        # Column name derived from URL
        column_name = url.split("/")[-1].replace(".php", "")

        r = requests.get(url, headers=HEADERS, timeout=30)
        soup = BeautifulSoup(r.text, "html.parser")

        containers = soup.find_all(
            "div", class_="picTrans recordsetContainer boxShadow zoom"
        )

        sub_countries, values = [], []

        for item in containers:
            try:
                sub_countries.append(
                    item.find("span", class_="textWhite textLarge textShadow").text.strip()
                )
                values.append(
                    item.find_all("span", class_="textWhite textLarge")[-1].text.strip()
                )
            except:
                continue

        # Metric-specific DataFrame
        df_sub = pd.DataFrame(
            {"country": sub_countries, column_name: values}
        )

        # Merge metric data with main DataFrame
        df_main = df_main.merge(df_sub, on="country", how="left")

    # ................ Clean numeric columns .....................
    for col in df_main.columns[2:]:
        cleaned = []
        for val in df_main[col]:
            if pd.isna(val):
                cleaned.append(None)
                continue

            # Remove commas/spaces and extract numeric value
            v = str(val).replace(",", "").replace(" ", "")
            m = re.search(r"-?\d+\.?\d*", v)
            cleaned.append(float(m.group()) if m else None)

        df_main[col] = cleaned

    return df_main



# Script execution
# ............................................
df = scrape_global_firepower_data()

# Save final dataset to CSV for further analysis and dashboards
df.to_csv("global_firepower_data_2025.csv", index=False)

# Preview first few rows
print(df.head())
