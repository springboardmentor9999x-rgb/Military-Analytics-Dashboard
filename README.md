# Strategic Defense Intelligence Platform (2025)

<p align="center">
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black" />
  <img src="https://img.shields.io/badge/Python-Data%20Pipeline-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/DAX-Coalition%20Modeling-orange" />
  <img src="https://img.shields.io/badge/Architecture-Star%20Schema-blue" />
  <img src="https://img.shields.io/badge/Infosys-Springboard%206.0-0078D4" />
</p>

---

<p align="center">
  <b>Unified Military Intelligence & Coalition Analysis System</b><br>
  Power BI • DAX • Coalition Analytics
</p>

---

# 📌 Project Overview

The **Strategic Defense Intelligence Platform (2025)** is a comprehensive Business Intelligence solution developed during the **Infosys Springboard Virtual Internship 6.0**.

This analytics engine transforms scattered global military datasets into actionable intelligence through:

* 🌐 Multi-nation strategic benchmarking
* 📈 Performance-driven KPI evaluations
* 💰 Budget optimization assessments
* ⚔️ Alliance force projection simulations
* 🚀 Real-time slicer-powered insights

Complete end-to-end pipeline from data extraction to interactive defense analytics.

---

# 🎯 Problem Statement

Public military datasets suffer from:

* Data trapped across fragmented sources
* No unified coalition analysis framework  
* Missing dynamic "what-if" alliance modeling
* Static KPIs without efficiency context
* Manual aggregation delays in threat scenarios

**This project delivers instant coalition strength simulation and gap analysis.**

---

# 🚀 Key Features

## 🔹 Intelligent Data Pipeline

* Python data extraction & transformation
* Multi-table star schema (5 core tables)
* 140+ countries | 60+ military metrics
* Clean numeric processing
* Year-specific 2025 analysis

## 🔹 Strategic KPI Framework

* Coalition Strength Delta (%)
* Budget Efficiency Ratio
* Personnel-to-Capability Index
* Domain Power Balance (Air/Land/Naval)
* Force Projection Score
* Alliance Readiness Multiplier
* Strategic Burden Metric
* Power Index Gap Analysis
* Coalition vs Reference Comparison
* Dynamic SUMX aggregation measures

## 🔹 Coalition Intelligence Engine

* Multi-select alliance builder
* Real-time strength recalculation
* Reference country benchmarking (USA baseline)
* Gap percentage visualization
* Domain-specific breakdowns

## 🔹 Advanced Data Architecture

* Star schema modeling
* DAX measure optimization
* Slicer-responsive calculations
* Virtual period intelligence
* Scalable coalition logic

---

# 🛠 Tech Stack

| Layer             | Technology                        |
| ----------------- | --------------------------------- |
| Data Source       | Military datasets (2025)         |
| Data Prep         | Python • Pandas                  |
| Data Model        | Star Schema (5 tables)           |
| BI Platform       | Power BI Desktop                 |
| Analytics         | DAX (15+ coalition measures)     |
| Visualization     | Gauges • Radar • Treemaps Charts  |

---

# 📊 Dashboard Showcase

## 🟡 Executive Summary

<p align="center">
  <img src="assets/Executive_Summary.png" width="800"/>
</p>

Key metrics:
* Coalition vs Reference totals
* Strategic gap percentages
* Global power distribution
* Readiness indicators

## 🔵 Country Intelligence

<p align="center">
  <img src="assets/Country_Intelligence.png" width="800"/>
</p>

Detailed views:
* Personnel pyramid (active/reserve)
* Budget efficiency ratios
* Domain strength profiles
* Geographic capability mapping

## 🟢 Power Comparison

<p align="center">
  <img src="assets/Power_Comparison.png" width="800"/>
</p>

Strategic analysis:
* Multi-domain radar charts
* Tornado gap visualization
* Stacked capability breakdown
* Reference benchmarking

## 🔴 Alliance Simulator

<p align="center">
  <img src="assets/Alliance_Simulator.png" width="800"/>
</p>

Live capabilities:
* Drag-and-drop coalition building
* Instant strength recalculation
* Delta gap cards (+15% stronger)
* Domain composition analysis

---

# 📈 Strategic Findings

Dashboard reveals critical insights:

* Budget size ≠ strategic effectiveness
* Regional alliances shift power balances
* Naval coalitions challenge air dominance
* Personnel efficiency varies 5x globally
* Small nations enable coalition specialization

**Example**: UK+France+Germany exceeds USA naval tonnage by 12% but trails air combat readiness.

---

# 🧠 Technical Architecture

## ⚙ Coalition-Aware Data Model

DimGeography → FactMilitary ← MilitaryBranches
↓              ↓              ↓
DimOrganization  DimPerformance  Coalition Measures Slicer-driven, fully dynamic aggregation.



**Core DAX Pattern** (15+ measures):
```dax
Coalition Naval Power = 
SUMX(
    VALUES(DimGeography[Country]),
    CALCULATE(SUM(FactMilitary[total_naval_fleet]), Year=2025)
)
```

**⚠ Technical Challenges**
Fragmented multi-source datasets
Coalition logic without physical joins
Numeric extraction from mixed formats
Complex DAX optimization for slicers
Real-time recalculation performance

Solutions:
Star schema normalization
SUMX/VALUES pattern innovation
Regex data cleaning pipeline
Measure optimization techniques

🔮 Future Enhancements
Multi-year trend analysis
Real-time API integration
ML-powered threat prediction
Mobile-responsive deployment
Granular asset-type drilldowns
Geospatial force mapping

🏁 Impact Summary: Strategic Defense Intelligence Platform proves mastery of:
✔ Complete BI pipeline engineering
✔ Advanced DAX coalition modeling
✔ Star schema optimization
✔ Real-time slicer intelligence
✔ Strategic visualization design
✔ End-to-end analytics solution

From raw military data → instant coalition supremacy analysis.


👤 Author
PRIYANKA DUTTA
Infosys Springboard Virtual Internship 6.0
Data Visualization & Analytics Track
