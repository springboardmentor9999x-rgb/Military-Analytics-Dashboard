import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re

# ------------------------------
# Global Config
# ------------------------------
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

DATASET_LINKS_FILE = "dataset_links.txt"
OUTPUT_DIR = "output"
OUTPUT_FILE = "global_military_raw_data.csv"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------
# Read metric URLs
# ------------------------------
def read_links_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip().startswith("http")]

# ------------------------------
# Fetch country list + ranks
# ------------------------------
def fetch_countries():
    url = "https://www.globalfirepower.com/countries-listing.php"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    countries = []
    ranks = []

    containers = soup.select("div.picTrans.recordsetContainer")

    for box in containers:
        try:
            country = box.find(
                "span", class_="textWhite textLarge textShadow"
            ).text.strip()

            rank = box.find(
                "span", class_="textWhite textLarge textBold"
            ).text.strip()

            countries.append(country)
            ranks.append(rank)
        except:
            continue

    return pd.DataFrame({
        "Country": countries,
        "Rank": ranks
    })

# ------------------------------
# Scrape one metric page
# ------------------------------
def scrape_metric_page(url):
    print(f"Scraping: {url}")

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.select("div.picTrans.recordsetContainer")

    countries = []
    values = []

    for row in rows:
        try:
            country = row.find(
                "span", class_="textWhite textLarge textShadow"
            ).text.strip()

            value = row.find_all(
                "span", class_="textWhite textLarge"
            )[-1].text.strip()

            countries.append(country)
            values.append(value)
        except:
            continue

    column_name = url.split("/")[-1].replace(".php", "")

    return pd.DataFrame({
        "Country": countries,
        column_name: values
    })

# ------------------------------
# MAIN PIPELINE
# ------------------------------
def main():
    metric_urls = read_links_txt(DATASET_LINKS_FILE)

    df = fetch_countries()

    for url in metric_urls:
        metric_df = scrape_metric_page(url)
        df = df.merge(metric_df, on="Country", how="left")

    # Basic numeric cleanup (still RAW for Task 1)
    for col in df.columns[2:]:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.extract(r"(\d+\.?\d*)")[0]
        )

    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    df.to_csv(output_path, index=False)

    print("\n✅ Data extraction completed successfully!")
    print("Total Countries:", len(df))
    print("Total Features:", len(df.columns))
    print("\nPreview:\n")
    print(df.head())

# ------------------------------
# ENTRY POINT
# ------------------------------
if __name__ == "__main__":
    main()
