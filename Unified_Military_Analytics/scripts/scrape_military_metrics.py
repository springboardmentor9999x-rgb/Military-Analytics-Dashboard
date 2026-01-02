import requests
import pandas as pd
from bs4 import BeautifulSoup


# STEP 1: Read links from file

links = []
with open("../data/links_for_military_data.txt", "r") as file:
    for line in file:
        if line.startswith("http"):
            links.append(line.strip())

# STEP 2: Get country list

base_url = "https://www.globalfirepower.com/countries-listing.php"
response = requests.get(base_url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

countries = []
ranks = []

boxes = soup.select("div.picTrans.recordsetContainer")

for box in boxes:
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
        pass

data = pd.DataFrame({
    "Country": countries,
    "Rank": ranks
})


# STEP 3: Scrape each metric

for url in links:
    print("Scraping:", url)

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.select("div.picTrans.recordsetContainer")

    metric_countries = []
    values = []

    for row in rows:
        try:
            country = row.find(
                "span", class_="textWhite textLarge textShadow"
            ).text.strip()

            value = row.find_all(
                "span", class_="textWhite textLarge"
            )[-1].text.strip()

            metric_countries.append(country)
            values.append(value)
        except:
            pass

    column_name = url.split("/")[-1].replace(".php", "")

    temp = pd.DataFrame({
        "Country": metric_countries,
        column_name: values
    })

    data = data.merge(temp, on="Country", how="left")


# STEP 4: Save output
data.to_csv("../data/military_metrics_week1.csv", index=False)

print("\n✅ Week 1 task completed")
print("Countries:", len(data))
print("Metrics:", len(data.columns) - 2)
print(data.head())
