# Unified Military Analytics and Comparison Dashboard

## 📌 Project Overview
This project is a full-stack data analytics solution designed to analyze global military power in 2025. It combines a **Python** backend for web scraping and data processing with a **Tableau** frontend for interactive visualization.

The system scrapes live data for 145 countries from GlobalFirepower.com, engineers 50+ key metrics, and visualizes them through a 4-page interactive dashboard suite that allows users to compare nations, analyze alliances, and assess global military strength.

## 🔗 Live Dashboard
**[👉 Click Here to View the Interactive Dashboard on Tableau Public](https://public.tableau.com/views/GlobalMilitaryPower-SHUBHAMKUMAR/AllianceSimulator?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**

---

## 📸 Dashboard Gallery

### 1. Global Stats (Home)
*A geospatial overview of global military spending and active personnel distributions.*
<img width="1919" height="976" alt="Quick Stats" src="https://github.com/user-attachments/assets/d65a6f58-9967-4743-8686-903fd7258d0c" />
### 2. Nation Overview
*Deep-dive profiling for individual countries with radar charts for balanced capability assessment.*
<img width="1919" height="975" alt="Nation Overview" src="https://github.com/user-attachments/assets/d49320e9-8e41-4eab-ae1e-da43845ad534" />
### 3. Compare Powers
*Dynamic competitive analysis engine comparing any two nations across air, land, and naval assets.*
<img width="1918" height="973" alt="Compare Powers" src="https://github.com/user-attachments/assets/76e7175b-d2b5-4776-8171-c2be2be8c4b3" />
### 4. Coalition Builder
*A custom aggregation tool allowing users to build hypothetical coalitions (e.g., NATO vs. BRICS) and calculate combined strength.*
<img width="1919" height="977" alt="Coalition Builder" src="https://github.com/user-attachments/assets/4b297dc7-2c43-4cb6-9b55-34669fd20988" />
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
- [✔️] **Milestone 1:** Data Scraping & Raw Data Generation
- [✔️] **Milestone 2:** KPI Engineering (Rank Gaps, Assets per Capita)
- [✔️] **Milestone 3:** Dashboard Development (Quick Stats, Nation Overview)
- [✔️] **Milestone 4:** Final Integration & Comparison Modules **(COMPLETED)**

## 👨‍💻 How to Run the Scraper
1. **Install Dependencies:**
   ```bash
   pip install pandas requests beautifulsoup4
Run the Script:

Bash
python scrape_military_metrics.py
