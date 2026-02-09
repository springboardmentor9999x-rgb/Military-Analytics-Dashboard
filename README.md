⚔️ Global Military Power Analysis & Alliance Simulator
A high-fidelity military intelligence dashboard analyzing the defense capabilities of 140+ nations. Features a dynamic "War Room" simulator for modeling hypothetical coalition conflicts.

📖 Project Overview
This project goes beyond simple data visualization to build an interactive Decision Support System (DSS) for military analysis. Built in Tableau, it processes complex geopolitical data—defense budgets, manpower, airpower, and naval assets—to answer critical questions about global security.

The core innovation is Dashboard 4 (The Alliance Simulator), which allows users to build custom "sandbox" coalitions (e.g., NATO + Japan) and test their combined strength against a specific rival nation in real-time.

📊 Dashboard Breakdown
1. 🌍 Quick Stats Dashboard
The Strategic View.

<img width="1919" height="976" alt="Quick Stats" src="https://github.com/user-attachments/assets/c8af9602-964e-4664-adab-061f7c26bf61" />

Key Insight: Instantly visualize the "Power Index" distribution across continents.

Features: Filter by Region/Alliance to see how power is concentrated globally.

2. 📈 Nation Overview Dashboard
The Data Correlation Engine.

<img width="1919" height="975" alt="Nation Overview" src="https://github.com/user-attachments/assets/28ca60f2-2fbc-4229-8df1-ec81d0ed855f" />

Key Insight: Analyzing the correlation between GDP vs. Defense Spending. Does money always buy military might?

Analysis: Outlier detection (identifying countries that punch above their weight class).

3. ⚔️ Compare Powers Dashboard
The Direct Comparator.

<img width="1918" height="973" alt="Compare Powers" src="https://github.com/user-attachments/assets/9f361cd4-5ec5-4b0d-ad52-61bf94b21a34" />

Functionality: Select Any Two Countries to see a side-by-side breakdown of their strengths (Air, Land, Sea, Finance).

Logic: Uses dynamic parameters to calculate the "Rank Gap" live.

4. 🛡️ Coalition Builder Dashboard ("War Room")
The Star Feature - A Sandbox Simulation.

Functionality: A "What-If" scenario builder.

User Action:

Select a Rival: (e.g., Russia).

Build a Coalition: Manually check boxes to form a team (e.g., USA + UK + France + Poland).

Simulate: The dashboard instantly calculates the Combined Coalition Strength vs. the Rival Target.

<img width="1919" height="977" alt="Coalition Builder" src="https://github.com/user-attachments/assets/5668ce75-7f7d-4b7e-8a34-312bcde3e680" />


⚙️ Technical "Under the Hood"
This project utilizes advanced Tableau features to create a seamless user experience:

Dynamic Sets: Used in Dashboard 4 to allow multi-select "Coalition Building" without filtering out the Rival data.

Parameter Actions: Used for switching between metrics (Troops, Budget, Tanks) dynamically.

Complex Calculated Fields:

Collision Detection: Logic to ensure a country cannot be in the Coalition AND be the Rival simultaneously.

Normalization: Logarithmic scaling for charts comparing massive disparities (e.g., USA Budget vs. Small Nations).

LOD Expressions (Level of Detail): Used to calculate Global Averages that remain fixed even when filtering specific regions.

🛠️ How to Use
Download the .twbx file.

Open in Tableau Desktop or Tableau Public.

Navigate to "Dashboard 4 - Alliance Simulator".

Test the Logic:

Set Rival to 'China'.

Use the Custom Set List to select 'India', 'Japan', and 'Australia'.

Watch the Map turn Blue/Red and the Bar Charts update instantly.

📂 Data Sources
Global Firepower Index (2024): Primary military strength data.

World Bank: Supplemental GDP and Population data.

Note: Data cleaning performed to standardize country names and currency conversions.
