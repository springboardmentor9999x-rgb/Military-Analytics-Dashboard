# Military Data KPI Generator

This module is designed to generate Key Performance Indicators (KPIs) from military data, process it into wide and long formats, enrich it with available metadata, and save the results into an Excel file. It also provides a standalone Python script to automate this entire process.

## Module Purpose

To provide a comprehensive analysis of military data by calculating various strategic and operational KPIs, enabling detailed comparison and trend analysis across different countries and their alliances.

## Generated KPIs

The module calculates the following 10 per-country KPIs:

1.  **Assets per Capita**: Military asset concentration relative to population size.
    *   Formula: `(total_aircraft + tanks + naval_assets) / population`

2.  **Defense Budget to GDP Ratio**: How much of a country’s economy is spent on defense.
    *   Formula: `defense_budget_usd / gdp_usd`

3.  **Personnel Density**: Share of population engaged in military service.
    *   Formula: `total_personnel / population`

4.  **Defense Budget per Soldier**: Investment per active military personnel.
    *   Formula: `defense_budget_usd / active_personnel`

5.  **Power Index Rank Gap**: Relative ranking difference between a country and the reference country (USA or rank-1 country).
    *   Formula: `power_index_rank - reference_country_rank`

6.  **Air Power Ratio**: Air asset concentration per soldier.
    *   Formula: `total_aircraft / active_personnel`

7.  **Armor Intensity Index**: Tank density across land area.
    *   Formula: `tanks / land_area_sq_km`

8.  **Naval Strength per Coastline**: Naval presence relative to coastline length.
    *   Formula: `naval_assets / coastline_km`

9.  **Military Burden Index**: Defense spending per citizen.
    *   Formula: `defense_budget_usd / population`

10. **Alliance-Based Coalition Strength Index**: Combined `total_assets` based on alliance affiliation.
    *   Formula: `SUM(total_assets)` for all countries within the same alliance. Defaults to individual `total_assets` for non-alliance members ('Other').

## Usage

To run the KPI generation and data processing:

1.  **Ensure Data is Available**: Make sure the `military_cleaned.csv` file is present in the `/content/` directory.

2.  **Run the Python Script**: Execute the `generate_kpis.py` script. This script will perform all necessary calculations and generate the output Excel file.

    ```bash
    python generate_kpis.py
    ```

    *Note: The script handles missing dependencies like `xlsxwriter` by installing them if not found.*

## Output Files

Upon successful execution, the module generates the following files:

*   **`military_final.xlsx`**: An Excel workbook containing two sheets:
    *   **`Wide Format KPIs`**: Each row represents a country, with columns for original features, all calculated KPIs (including 'Alliance-Based Coalition Strength Index'), and metadata.
    *   **`Long Format KPIs`**: KPIs are stacked into a single 'KPI' column with their corresponding 'Value' in another column, along with country identifiers and metadata. This format is ideal for detailed comparative analysis in tools like Tableau.

*   **`generate_kpis.py`**: A Python script encapsulating all the logic from data loading to KPI calculation and output saving. This script is designed to be runnable independently for reproducibility and automation.
