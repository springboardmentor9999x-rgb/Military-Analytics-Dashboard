# ⚔️ Unified Military Analytics & Alliance Simulator (2025)

![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-yellow?style=for-the-badge&logo=powerbi)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Complete-green?style=for-the-badge)

## 📖 Project Overview
This project is an interactive **Military Intelligence Decision Support System**. It transforms raw defense data (scraped via Python from GlobalFirepower) into normalized strategic insights. The dashboard is designed to analyze not just "who has the most," but the **economic efficiency** and **military doctrine** of 140+ nations.

---

## 📊 Dashboard Modules & Strategic Insights

### 1. 🌍 Global Intelligence (Quick Stats)
**The Strategic View:** This page provides a macro-level overview of global power distribution.
*   **Key Visuals:** Global Power Map, Spending vs. Wealth Scatter Plot, and Top 10 Power Rankings.
*   **Strategic Metric:** **Assets per Capita** (16.23 in the screenshot) — This normalizes military hardware against the population to show how "militarized" a nation truly is.
*   **Observation:** The **Spending vs. Wealth** chart identifies outliers that are spending significantly more than their GDP suggests is sustainable.

![Quick Stats](quick_stats.png)

---

### 2. 📈 Nation Overview (Deep Dive)
**The Doctrine Engine:** Analyzes the specific "DNA" of a single country's military forces.
*   **Key Visuals:** National Asset Profile, Readiness Mix (Active vs. Reserve), and Ground Power Funnel.
*   **Strategic Insight:** Using **India** as an example, the dashboard reveals a balanced doctrine with a massive **55% Active to 44% Reserve** personnel ratio, supported by a heavy concentration of armored vehicles.
*   **Functionality:** Allows users to see a country's **Global Power Rank** (e.g., Rank 4) and its alliance status instantly.

![Nation Overview](nation_overview.png)

---

### 3. ⚔️ Compare Powers (Versus Mode)
**The Tactical Duel:** A direct benchmarking tool for regional rivals.
*   **Key Visuals:** Side-by-side comparison of Budget, Personnel, and Total Assets.
*   **Strategic Metric:** **Rank Gap** (57 in the screenshot) — This quantifies the parity between two nations (e.g., Austria vs. Brazil).
*   **Logic:** Uses a "Disconnected Table" DAX pattern to allow two independent country selections on a single screen without filter conflict.

![Compare Powers](compare_powers.png)

---

### 4. 🛡️ Coalition Builder (War Room)
**The Alliance Simulator:** A "What-If" tool for modeling group strength.
*   **Key Visuals:** Coalition Gauge Chart, Alliance Asset Breakdown (Treemap), and Member Contribution.
*   **Innovation:** This module aggregates the assets of a user-selected group (e.g., *Australia + Brazil + China*) to see if they can reach the target strength of a **Reference Superpower**.
*   **Outcome:** The **Coalition Assets Gauge** provides a real-time visual of how close an alliance is to achieving tactical parity with a global leader.

![Coalition Builder](coalition_builder.png)

---

## 🛠️ Technical Engineering
*   **Data Pipeline:** Python scripts for scraping and cleaning 50+ military indicators.
*   **KPI Engineering:** Advanced DAX formulas including:
    *   `Assets per Million = (Total Assets / Population) * 1,000,000`
    *   `Economic Burden = Defense Budget / GDP`
    *   `Rank Gap = ABS([Rank1] - [Rank2])`
*   **UI/UX:** Consistent 2x2 grid layout, custom topographical themes, and integrated page navigation.

## 📂 Folder Structure
- `notebooks/`: Python logic for data extraction and cleaning.
- `data/`: Final processed datasets (CSV/XLSX).
- `dashboards/`: The `.pbix` source file for local review.

---
*Created for the Unified Military Analytics Project - 2025*
