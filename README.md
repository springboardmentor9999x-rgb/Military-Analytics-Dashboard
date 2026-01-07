
## 📌 Project Overview

This project is part of **Week 1 -- Web Scraping Task**.\
The goal is to collect **country-level military data** from
**GlobalFirepower.com** and store it in a structured CSV file.

The project scrapes multiple military metrics such as: - Population -
Military manpower - Aircraft - Tanks - Naval strength - Defense budget

All collected data is merged **country-wise** into a single CSV file.

------------------------------------------------------------------------

## 📂 Project Folder Structure

Unified_Military_Analytics/ 

│ ├── scripts/ 

│ └──scrape_military_metrics.py 

│ ├── data/ 

│ ├── links_for_military_data.txt

│ └── military_metrics_week1.csv

| └── README.md


------------------------------------------------------------------------

## 📄 Input File Explanation

### 🔹 links_for_military_data.txt

**Location:** data/\
This file contains all dataset URLs (one per line) taken from
GlobalFirepower.com.

Example:
https://www.globalfirepower.com/total-population-by-country.php\

https://www.globalfirepower.com/available-military-manpower.php\

https://www.globalfirepower.com/aircraft-total.php

------------------------------------------------------------------------

## 🧠 How the Code Works

### Step 1: Read URLs

The script reads all dataset links from the text file so links can be
updated without changing code.

### Step 2: Fetch Countries

The script collects country names and global ranks from the countries
listing page.

### Step 3: Scrape Metrics

Each metric page is scraped and merged with the main dataset using
country names.

### Step 4: Save Output

The final dataset is saved as: data/military_metrics_week1.csv

------------------------------------------------------------------------

## 📊 Output File

Each row represents a country.\
Each column represents a military metric.

The output CSV is ready for: - Analysis - Dashboards - Comparisons

------------------------------------------------------------------------

## ▶️ How to Run

1.  Open Command Prompt\
2.  Navigate to scripts folder\
3.  Run: python scrape_military_metrics.py

------------------------------------------------------------------------

## 📸 Screenshots (Add in GitHub)

OutPut:
<img width="819" height="281" alt="image" src="https://github.com/user-attachments/assets/caded279-bffd-4112-a2de-0f72ddb90dfa" />


------------------------------------------------------------------------

## 🔗 References

-   https://www.globalfirepower.com
-   Python, Requests, BeautifulSoup, Pandas

------------------------------------------------------------------------

