# Unified Military Analytics and Comparison Dashboard

## 📌 Project Overview
This project is a full-stack data analytics solution designed to analyze global military power in 2025. It combines a **Python** backend for web scraping and data processing with a **Tableau** frontend for interactive visualization.

The system scrapes live data for 145 countries from GlobalFirepower.com, engineers 50+ key metrics, and visualizes them through a 4-page interactive dashboard suite that allows users to compare nations, analyze alliances, and assess global military strength.

## 🔗 Live Dashboard
**[👉 Click Here to View the Interactive Dashboard on Tableau Public](https://public.tableau.com/views/GlobalMilitaryPower-SHUBHAMKUMAR/AllianceSimulator?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**

---

## 📸 Dashboard Gallery

### 1. Global Command Center (Home)
*A geospatial overview of global military spending and active personnel distributions.*
<img width="1919" height="977" alt="Screenshot 2026-02-02 004719" src="https://github.com/user-attachments/assets/05edce5a-ee9b-4437-834e-0e3bfb5c6cfd" />
### 2. Nation Inspector
*Deep-dive profiling for individual countries with radar charts for balanced capability assessment.*
<img width="1919" height="974" alt="Screenshot 2026-02-02 004739" src="https://github.com/user-attachments/assets/370ffd95-1b2f-4365-9289-3df14d3b59a9" />
### 3. Head-to-Head Comparison
*Dynamic competitive analysis engine comparing any two nations across air, land, and naval assets.*
<img width="1919" height="978" alt="Screenshot 2026-02-02 004807" src="https://github.com/user-attachments/assets/7f4e4669-c6e5-4a11-b42f-8d3ba48ce3a8" />
### 4. Alliance Simulator
*A custom aggregation tool allowing users to build hypothetical coalitions (e.g., NATO vs. BRICS) and calculate combined strength.*
<img width="1919" height="973" alt="Screenshot 2026-02-02 004925" src="https://github.com/user-attachments/assets/1ecfff18-996b-4bed-b3c9-18e1a37680a1" />
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
