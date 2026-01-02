🌍 Unified Military Analytics & Comparison Dashboard
📊 A Comprehensive Data Engineering & Analytics Project

Author: Rutuja Ghodake
Tools Used: Python, BeautifulSoup, Pandas, Git, GitHub

📌 Project Overview

The Unified Military Analytics & Comparison Dashboard is a data-driven project designed to collect, process, and analyze global military data from GlobalFirepower.com.

This project automates the extraction of country-wise military metrics such as manpower, personnel strength, and other defense indicators. The cleaned and structured data is then prepared for advanced analysis and visualization.

This project demonstrates:

Real-world web scraping

Data cleaning & transformation

Structured data engineering workflow

Industry-level Git version control practices

🎯 Project Objectives

Extract military data from multiple webpages

Automate data collection using Python

Clean and normalize raw HTML data

Combine multiple datasets into a single structured CSV

Prepare data for analytics and dashboards (Power BI / Tableau)

🧰 Tech Stack & Tools Used
Category	Tools
Programming	Python
Web Scraping	requests, BeautifulSoup
Data Handling	pandas
Version Control	Git, GitHub
IDE	VS Code
Data Storage	CSV Files

📁 Project Structure
Unified_Military_Analytics/
│
├── links_for_global_military_data.txt   # List of all data source URLs
├── global_military_data.csv             # Final cleaned dataset
├── scrape_military_data.py              # Main scraping script
├── README.md                            # Project documentation

🔍 How the Project Works
Step 1: URL Collection

All relevant GlobalFirepower URLs are stored in a .txt file.
Each URL represents a specific military metric (manpower, equipment, budget, etc.).

Step 2: Web Scraping

The script:

Sends HTTP requests using requests

Parses HTML using BeautifulSoup

Extracts:

Country names

Military metric values

Handles missing data gracefully

Step 3: Data Cleaning

Removes unwanted characters

Normalizes numeric values

Ensures consistent country naming

Merges all metrics into a single DataFrame

Step 4: Output Generation

Final structured dataset is saved as:

global_military_data.csv


This file is ready for:

Power BI dashboards

Tableau visualization

Further analytics or ML modeling

🚀 How to Run the Project
1️⃣ Install Dependencies
pip install requests beautifulsoup4 pandas

2️⃣ Run the Script
python scrape_military_data.py

3️⃣ Output

A CSV file will be generated in the project directory.

🧠 Key Learnings

✔ Real-world web scraping
✔ Handling dynamic HTML structures
✔ Cleaning inconsistent data
✔ Managing Git branches and commits
✔ Professional project organization

🏆 Outcome

This project demonstrates:

End-to-end data engineering workflow

Clean coding practices

Real-world problem-solving ability

Strong understanding of data extraction pipelines

📌 Future Enhancements

Add retry logic & error handling

Automate periodic data updates

Integrate Power BI dashboards

Deploy as a scheduled ETL pipeline

🙌 Acknowledgment

This project was developed as part of a learning initiative to build industry-level data engineering skills.

✨ Thank you for reviewing this project!
If you have feedback or suggestions, feel free to share.



