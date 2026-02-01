# Unified Military Analytics and Comparison Dashboard

## 📌 Project Overview
This project is a full-stack data analytics solution designed to analyze global military power in 2025. It combines a **Python** backend for web scraping and data processing with a **Tableau** frontend for interactive visualization.

The system scrapes live data for 145 countries from GlobalFirepower.com, engineers 50+ key metrics, and visualizes them through a 4-page interactive dashboard suite that allows users to compare nations, analyze alliances, and assess global military strength.

## 🔗 Live Dashboard
**[👉 Click Here to View the Interactive Dashboard on Tableau Public](#)** *(Replace this # with your actual Tableau Public link)*

---

## 📸 Dashboard Gallery

### 1. Global Command Center (Home)
*A geospatial overview of global military spending and active personnel distributions.*
![Global Quick Stats](https://github.com/user-attachments/assets/PLACEHOLDER_FOR_IMAGE_1)
### 2. Nation Inspector
*Deep-dive profiling for individual countries with radar charts for balanced capability assessment.*
![Nation Inspector](https://github.com/user-attachments/assets/PLACEHOLDER_FOR_IMAGE_2)
### 3. Head-to-Head Comparison
*Dynamic competitive analysis engine comparing any two nations across air, land, and naval assets.*
![Head-to-Head](https://github.com/user-attachments/assets/PLACEHOLDER_FOR_IMAGE_3)
### 4. Alliance Simulator
*A custom aggregation tool allowing users to build hypothetical coalitions (e.g., NATO vs. BRICS) and calculate combined strength.*
![Alliance Simulator](https://github.com/user-attachments/assets/PLACEHOLDER_FOR_IMAGE_4)
---

## 🚀 Key Features
* **Automated Data Pipeline:** Python script scrapes, cleans, and structures data for 145 nations.
* **Dynamic Comparison Logic:** Tableau Parameters enable "Select A vs. Select B" analysis with instant variance calculation.
* **Geospatial Intelligence:** Interactive map layers showing defense spending density and regional power balances.
* **Set Action Logic:** "Alliance Simulator" uses Tableau Set Actions to aggregate data for user-selected groups of countries.
* **Custom UI/UX:** Dark-mode aesthetic with custom navigation bar for a seamless app-like experience.

## 📂 Repository Structure
* `scrape_military_metrics.py`: The main Python script for web scraping.
* `links_for_military_data.txt`: Source file containing URLs and column mappings.
* `military_final_data.csv`: The processed dataset used for the dashboard.
* `Global_Military_Power_2025.twbx`: The packaged Tableau workbook.

## 🛠️ Tech Stack
* **Data Collection:** Python (BeautifulSoup, Requests)
* **Data Manipulation:** Pandas (Cleaning, Ranking, KPI Generation)
* **Visualization:** Tableau Public (Parameters, Calculated Fields, Set Actions)

## 📅 Roadmap Status
- [x] **Milestone 1:** Data Scraping & Raw Data Generation
- [x] **Milestone 2:** KPI Engineering (Rank Gaps, Assets per Capita)
- [x] **Milestone 3:** Dashboard Development (Quick Stats, Nation Overview)
- [x] **Milestone 4:** Final Integration & Comparison Modules **(COMPLETED)**

## 👨‍💻 How to Run the Scraper
1. **Install Dependencies:**
   ```bash
   pip install pandas requests beautifulsoup4
Run the Script:

Bash
python scrape_military_metrics.py
