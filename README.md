# Unified Military Analytics and Comparison Dashboard

## 📌 Project Overview
This project aims to develop a fully interactive dashboard suite for analyzing global military power in 2025. The system scrapes data for 140+ countries from GlobalFirepower.com, processes it into key performance indicators (KPIs), and visualizes it through an interactive dashboard.

## 🚀 Current Status: Milestone 1 Completed
**Focus:** Data Collection and Preparation
- [x] Developed a Python script to scrape 50+ military metrics for 140+ countries.
- [x] Successfully handled data cleaning (removed special characters, formatted numbers).
- [x] Generated the raw dataset: `military_raw_data.csv`.

## 📂 Repository Structure
- `scrape_military_metrics.py`: The main Python script for web scraping.
- `links_for_military_data.txt`: The source file containing URLs and column mappings.
- `military_raw_data.csv`: The output dataset containing the scraped military metrics.

## 🛠️ How to Run
1. **Install Dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install pandas requests beautifulsoup4
Run the Scraper:

Bash

python scrape_military_metrics.py
The script will read links from the text file and generate/overwrite military_raw_data.csv.

📅 Roadmap

[✔️] Milestone 1: Data Scraping & Raw Data Generation

[ ] Milestone 2: KPI Engineering (Rank Gaps, Assets per Capita)

[ ] Milestone 3: Dashboard Development (Quick Stats, Nation Overview)

[ ] Milestone 4: Final Integration & Comparison Modules
