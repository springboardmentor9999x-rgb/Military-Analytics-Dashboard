# Military Analytics Dashboard – Data Collection

## Contributor
Sania Sayed

## Program Context
This project is developed as part of the **Infosys Springboard** learning program, focusing on hands-on data collection and preparation for analytics and dashboard development.

## Project Overview
This module focuses on collecting structured, country-level military and related data for the Military Analytics Dashboard project.

The data is sourced from publicly available Global Firepower pages and consolidated into a single analytics-ready dataset for further analysis and visualization.

## Learning Objectives
- Practice web scraping using Python
- Understand multi-source data collection
- Perform data cleaning and consolidation
- Prepare structured datasets for analytics workflows

## Data Sources
The source URLs are listed in the following file:
- `links_for_military_data.txt`

Each link corresponds to a specific military, economic, or infrastructure metric such as submarines, defense budget, oil reserves, or transportation coverage.

## Data Collection Approach
1. Source URLs are maintained in a TXT file for transparency and reproducibility.
2. Each URL is scraped using Python with `requests` and `BeautifulSoup`.
3. Country-wise values are extracted from each metric page.
4. All metrics are merged into a single dataset using the country name as the key.
5. Numeric values are cleaned and standardized.
6. The final dataset is saved as a CSV file for analysis and visualization.

## Files Description
- `military_webscraping.py` – Python script used to scrape and merge data from multiple sources.
- `links_for_military_data.txt` – List of Global Firepower URLs used as data sources.
- `military_raw_data.csv` – Final consolidated dataset generated from the scraping process.

## Output
The final output is a structured CSV file that can be directly used in tools like Power BI, Tableau, or Python-based analytics workflows.

## Notes
This repository focuses on data collection as part of the learning exercise. Further analysis and dashboard development will be handled in subsequent stages of the project.

Data Cleaning and Preprocessing (Task 2)

This module focuses on cleaning and preparing the raw military dataset collected during the web scraping stage.

The raw dataset contained inconsistencies such as missing values, duplicate records, inconsistent column naming, and non-uniform data types, which needed to be resolved before analysis and visualization.

Objectives

Clean and standardize the raw military dataset

Handle missing and invalid values

Ensure consistent data types for numerical analysis

Prepare an analytics-ready dataset

Data Cleaning Steps

Standardized column names to lowercase with underscores

Handled missing values by imputing defaults where appropriate

Removed duplicate country records

Converted all numeric fields to proper data types

Removed meaningless rows containing only zero values

Tools & Technologies

Python

Pandas library

Google Colab

Files Description

Task2_Military_Data_Cleaning.ipynb – Notebook containing the data cleaning and preprocessing steps

Task2_Data_Cleaning.csv – Final cleaned dataset ready for analysis

Output

The cleaned dataset is structured, consistent, and suitable for exploratory data analysis, machine learning, and dashboard development using tools such as Power BI, Tableau, or Python-based visualization libraries.
