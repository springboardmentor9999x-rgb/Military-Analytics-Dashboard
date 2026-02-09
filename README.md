# ⚔️ Global Military Power Analysis & Alliance Simulator

![Tableau](https://img.shields.io/badge/Tableau-2024.2-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

> **A high-fidelity military intelligence dashboard analyzing the defense capabilities of 140+ nations. Features a dynamic "War Room" simulator for modeling hypothetical coalition conflicts.**

---

## 📖 Project Overview
This project goes beyond simple data visualization to build an interactive **Decision Support System (DSS)** for military analysis. Built in **Tableau**, it processes complex geopolitical data-defense budgets, manpower, airpower, and naval assets-to answer critical questions about global security.

The core innovation is **Dashboard 4 (The Alliance Simulator)**, which allows users to build custom "sandbox" coalitions (e.g., *NATO + Japan*) and test their combined strength against a specific rival nation in real-time.

---

## 📊 Dashboard Breakdown

### 1. 🌍 Quick Stats Dashboard
*The Strategic View.*
* **Visuals:** 
<img width="1919" height="976" alt="Quick Stats" src="https://github.com/user-attachments/assets/06f96719-fb96-4a5b-bb00-ae44edcd6cc0" />

* **Key Insight:** Instantly visualize the "Power Index" distribution across continents.
* **Features:** Filter by Region/Alliance to see how power is concentrated globally.

### 2. 📈 Nation Overview Dashboard
*The Data Correlation Engine.*
* **Visuals:**
<img width="1919" height="975" alt="Nation Overview" src="https://github.com/user-attachments/assets/77d3214f-a07c-44d6-a64c-2e0449224a63" />

* **Key Insight:** Analyzing the correlation between **GDP vs. Defense Spending**. Does money always buy military might?
* **Analysis:** Outlier detection (identifying countries that punch above their weight class).

### 3. ⚔️ Compare Powers Dashboard
*The Direct Comparator.*
* **Visuals:**
<img width="1918" height="973" alt="Compare Powers" src="https://github.com/user-attachments/assets/0c9cb523-9333-41b2-b08c-f7c0cb81711f" />

* **Functionality:** Select **Any Two Countries** to see a side-by-side breakdown of their strengths (Air, Land, Sea, Finance).
* **Logic:** Uses dynamic parameters to calculate the "Rank Gap" live.

### 4. 🛡️ Coalition Builder Dashboard ("War Room")
*The Star Feature - A Sandbox Simulation.*
* **Functionality:** A "What-If" scenario builder.
* **User Action:**
    1.  **Select a Rival:** (e.g., *Russia*).
    2.  **Build a Coalition:** Manually check boxes to form a team (e.g., *USA + UK + France + Poland*).
    3.  **Simulate:** The dashboard instantly calculates the **Combined Coalition Strength** vs. the **Rival Target**.
* **Visuals:**
<img width="1919" height="977" alt="Coalition Builder" src="https://github.com/user-attachments/assets/fed1a61a-8709-4ce0-a4ec-1aead5d6db37" />


---

## ⚙️ Technical "Under the Hood"
This project utilizes advanced Tableau features to create a seamless user experience:

* **Dynamic Sets:** Used in Dashboard 4 to allow multi-select "Coalition Building" without filtering out the Rival data.
* **Parameter Actions:** Used for switching between metrics (Troops, Budget, Tanks) dynamically.
* **Complex Calculated Fields:**
    * *Collision Detection:* Logic to ensure a country cannot be in the Coalition AND be the Rival simultaneously.
    * *Normalization:* Logarithmic scaling for charts comparing massive disparities (e.g., USA Budget vs. Small Nations).
* **LOD Expressions (Level of Detail):** Used to calculate Global Averages that remain fixed even when filtering specific regions.

---

## 🛠️ How to Use
1.  **Download** the `.twbx` file.
2.  **Open** in Tableau Desktop or Tableau Public.
3.  **Navigate** to "Dashboard 4 - Alliance Simulator".
4.  **Test the Logic:**
    * Set **Rival** to 'China'.
    * Use the **Custom Set List** to select 'India', 'Japan', and 'Australia'.
    * Watch the **Map** turn Blue/Red and the **Bar Charts** update instantly.

---

## 📂 Data Sources
* **Global Firepower Index (2024):** Primary military strength data.
* **World Bank:** Supplemental GDP and Population data.
* *Note: Data cleaning performed to standardize country names and currency conversions.*

---

## 📄 License
Distributed under the MIT License. See below for more information.

---

### The MIT License (MIT)

**Copyright (c) 2026 SHUBHAM KUMAR**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
