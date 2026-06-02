# BLUESTOCK_MF_CAPSTONE

## Overview

This project is part of my Data Analyst Internship at Bluestock Fintech. The objective is to perform Mutual Fund data ingestion, validation, cleaning, exploration, and analysis using Python, Pandas, SQL, and data visualization tools.

---

## Project Structure

```text
BLUESTOCK_MF_CAPSTONE/

├── data/
│   ├── raw/
│   └── processed/
│
├── dashboard/
│
├── notebooks/
│   ├── 01_data_ingestion.py
│   ├── 02_data_cleaning.ipynb
│   └── 03_eda_analysis.ipynb
│
├── scripts/
│   ├── live_nav_fetch.py
│   └── batch_nav_fetch.py
│
├── report/
│
├── sql/
│
├── README.md
└── requirements.txt
```

---

## Objectives

* Load and inspect Mutual Fund datasets.
* Perform data validation and quality checks.
* Fetch live NAV data using MFAPI.
* Process and clean financial datasets.
* Explore Mutual Fund scheme information.
* Validate AMFI scheme codes.
* Prepare data for visualization and dashboard development.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Jupyter Notebook
* PostgreSQL
* Matplotlib
* Seaborn
* Plotly
* Requests
* Git & GitHub

---

## Tasks Completed

### Task 3 – Data Ingestion

* Loaded all provided CSV datasets.
* Checked dataset shape, columns, and data types.
* Performed initial data inspection.
* Identified missing values and anomalies.

### Task 4 – Live NAV Fetch

* Retrieved live NAV data from MFAPI.
* Parsed JSON response.
* Converted data into Pandas DataFrame.
* Saved NAV data as CSV.

### Task 5 – Batch NAV Fetch

* Retrieved NAV history for multiple mutual fund schemes.
* Stored scheme-wise CSV files.

### Task 6 – Fund Master Exploration

* Analyzed fund houses.
* Explored categories and sub-categories.
* Reviewed risk classifications.

### Task 7 – AMFI Validation

* Compared AMFI codes across datasets.
* Calculated dataset coverage.
* Generated validation summary.

---

## Data Sources

* Kaggle Mutual Fund Dataset
* MFAPI (https://api.mfapi.in)

---

## Future Work

* Advanced EDA
* SQL Analytics
* Dashboard Development
* Flask API Integration
* Capstone Report Generation

---

## Author

Arush Padmawar

Data Analyst Intern – Bluestock Fintech
