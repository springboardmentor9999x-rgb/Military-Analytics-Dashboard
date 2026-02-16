# 🛡️ Unified Military Analytics & Comparison Dashboard
### Web Scraping • Data Engineering • Power BI Analytics

The Unified Military Analytics & Comparison Dashboard is an end-to-end data analytics project that automates the collection, cleaning, transformation, and visualization of global military strength data.

The project scrapes raw military data from GlobalFirepower.com, converts unstructured web data into a clean and standardized dataset using Python, and presents insights through an interactive Power BI dashboard. It enables country-level analysis, military power comparison, and coalition-based strength evaluation.

---

## 📌 Project Overview

This project is designed as a complete data pipeline and analytics solution.

- Automated web scraping for 145 countries
- Cleaning and normalization of raw military data
- KPI engineering and metric standardization
- Interactive dashboards built using Power BI

The system allows users to move from raw web data to actionable strategic insights.

---

## 🎯 Project Objectives

- Automate large-scale military data collection
- Clean and normalize inconsistent web data
- Standardize numeric and categorical formats
- Merge multiple metric tables into a unified dataset
- Generate analytics-ready CSV and Excel files
- Build interactive Power BI dashboards
- Enable country comparison and coalition analysis

---

## 🧠 What This Project Includes

✔ Country-wise military strength data  
✔ Active, reserve, and total military personnel  
✔ Airpower, land forces, and naval assets  
✔ Defense budgets and economic indicators  
✔ Power Index and Assets per Capita metrics  
✔ Cleaned and standardized datasets  
✔ Fully interactive Power BI dashboards  

---

## 📊 Power BI Dashboard Pages

### 1️⃣ Quick Stats (Global Overview)
- Global military ranking and power index
- Total defense budget and military burden index
- Top countries by total military assets
- Alliance-wise defense budget distribution
- Economic power vs military strength analysis
  <img width="1394" height="810" alt="image" src="https://github.com/user-attachments/assets/25146c9d-bb81-48ff-b5a7-ba7c6c9f46c3" />


---

### 2️⃣ Nation Overview
- Detailed country-level analysis
- Power Index Score
- Defense Budget (USD)
- Total Military Personnel
- Assets per Capita
- Air, Land, and Naval power breakdown
  <img width="1377" height="817" alt="image" src="https://github.com/user-attachments/assets/67cf352e-6e8b-4a2b-916d-ce7dc239ba3f" />


---

### 3️⃣ Compare Powers
- Dynamic Country A vs Country B comparison
- Power Index A vs Power Index B
- Defense Budget A vs Defense Budget B
- Visual military asset comparison
- Real-time interactive slicers
  <img width="1364" height="820" alt="image" src="https://github.com/user-attachments/assets/817e1a47-fb64-4739-a20d-bb5a9213be76" />


---

### 4️⃣ Coalition Builder
- Build custom military alliances
- Aggregate defense budgets for selected countries
- Calculate combined total military assets
- Coalition-level military strength analysis
  <img width="1347" height="814" alt="image" src="https://github.com/user-attachments/assets/1c8f6a23-1a98-4538-a76e-665a6121a4b2" />


---

## 🔄 Data Pipeline & Workflow

### 1️⃣ Collect URLs
All metric URLs from GlobalFirepower are stored in a text file.

### 2️⃣ Scrape Data
Python scripts fetch HTML pages using requests and extract values using BeautifulSoup.

### 3️⃣ Clean & Normalize Data
- Remove commas, symbols, and mixed text
- Convert values to numeric formats
- Standardize country names and metrics

### 4️⃣ Merge DataFrames
All extracted metrics are merged using the Country column as the primary key.

### 5️⃣ Export Final Output
Clean datasets are exported as CSV and Excel files.

### 6️⃣ Power BI Integration
Processed data is loaded into Power BI where KPIs, measures, and dashboards are created.

---

## 📂 Repository Structure
├── All_links.txt
├── Dashboard.pbix
├── Global_military_data.csv
├── global_military_data_collection.ipynb
├── Unified_Military_Data.ipynb
├── Unified_Military_Data_Analytics.ipynb
├── military_final.xlsx
├── military_kpi_output.xlsx
├── Unified_Military_StandardizedData/
└── README.md


---

## 🧰 Technology Stack

**Data Collection & Engineering**
- Python
- Requests
- BeautifulSoup
- Pandas
- NumPy

**Analytics & Visualization**
- Power BI
- DAX
- Power Query
- Interactive slicers and measures

**Tools**
- Git & GitHub
- VS Code

---

## 👨‍💻 How to Run the Project

### 1️⃣ Install Dependencies

### 2️⃣ Run the Scraper

### 3️⃣ Open the Dashboard
- Open Dashboard.pbix in Power BI Desktop
- Refresh the dataset if required

---

## 🧠 Key Learnings

- Real-world web scraping and HTML parsing
- Cleaning and standardizing large datasets
- Building complete data pipelines
- KPI engineering and metric creation
- Creating interactive Power BI dashboards

---

## ⚠️ Disclaimer
This project is developed strictly for educational and analytical purposes. All data is sourced from publicly available information and does not represent official or classified military assessments.

---

## 👤 Author

Sonu Gupta  
Python • Web Scraping • Data Engineering • Power BI Analytics

---

## ⭐ Support
If you find this project useful, feel free to star the repository or fork it for further improvements.


