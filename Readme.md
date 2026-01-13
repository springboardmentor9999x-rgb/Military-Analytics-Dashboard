# 🛡️ Unified Military Analytics & Comparison Dashboard
### Web Scraping • Data Engineering • Analytics

The **Unified Military Analytics & Comparison Dashboard** is an end-to-end data extraction and analytics project built to gather, clean, and organize military strength information from **GlobalFirepower.com**. It converts unstructured web data into a structured and analysis-ready dataset, enabling comparisons between countries and powering dashboards or visualization tools.

---

## 📌 Project Overview

This project focuses on automating large-scale data collection and cleaning.  
It extracts multiple military metrics such as manpower, aircraft, land forces, naval strength, and economic indicators.  
After scraping, all metrics are merged into a single unified dataset, which is then exported as a clean CSV file.

---

## 🎯 Key Objectives

- Collect military-related metrics from multiple online sources  
- Clean and normalize raw HTML data  
- Standardize formats and numeric values  
- Merge all metric tables into one structured DataFrame  
- Produce an analytics-ready CSV file  
- Automate the entire scraping workflow  

---

## 🧠 What This Project Includes

✔ Country-level military strength  
✔ Active, reserve, and total manpower  
✔ Airpower, land systems, and naval assets  
✔ Economic and geographic indicators  
✔ Cleaned and normalized dataset  
✔ Automated scraping pipeline  

---

## 🧰 Technology Stack

| Tool | Purpose |
|------|---------|
| Python | Core scripting logic |
| Requests | Fetching HTML pages |
| BeautifulSoup | Parsing and extracting data |
| Pandas | Cleaning and merging datasets |
| Git & GitHub | Version control |
| VS Code | Development environment |

---

## 🔄 Workflow Overview

### **1️⃣ Collect URLs**
All metric URLs from GlobalFirepower are stored in a text file.

### **2️⃣ Scrape Data**
Each page is fetched using `requests`, and relevant values are extracted using BeautifulSoup.

### **3️⃣ Clean Data**
Symbols, commas, and mixed text are removed.  
All values are converted to clean numeric types.

### **4️⃣ Merge DataFrames**
All extracted metrics are joined together using the `Country` column as the unique key.

### **5️⃣ Export Final Output**
A structured CSV file is generated containing all indicators.

---

## 📊 Sample Output (Preview)

| Country | Rank | Active Personnel | Reserve | Equipment |
|--------|------|------------------|---------|-----------|
| India  | 4    | 1,455,550        | 1,155,000 | 4,000+ |
| USA    | 1    | 1,390,000        | 850,000   | 5,000+ |

*(Actual dataset contains dozens of additional metrics.)*

---

## 🧠 Key Learnings

- Real-world web scraping and HTML parsing  
- Cleaning inconsistent and incomplete data  
- Designing modular and reusable Python functions  
- Using Git for version control and collaboration  
- Understanding full data pipeline creation  

---

## 👤 Author

**Sonu Gupta**  
Web Scraping • Python Development • Data Analytics  

---

