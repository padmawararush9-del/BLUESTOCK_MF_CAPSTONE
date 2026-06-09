# Mutual Fund Analytics Project

## Overview

The Mutual Fund Analytics Project is an end-to-end data analytics and business intelligence solution developed to analyze mutual fund performance, investor behaviour, and industry trends. The project combines Python, SQL, and Power BI to perform data processing, financial analysis, advanced analytics, and dashboard development.

The objective of the project is to transform raw mutual fund data into actionable insights through performance metrics, risk analysis, investor analytics, and interactive visualizations.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SQL
* Power BI
* Jupyter Notebook
* Git & GitHub

---

## Project Structure
bluestock_mf_capstone/
├── data/
│   ├── raw/           ← original downloaded files
│   ├── processed/     ← cleaned, merged CSVs
│   └── db/            ← bluestock_mf.db (SQLite)
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── batch_nav_fetch.py
│   └── recommender.py
├── sql/
│   ├── schema.sql
│   └── queries.sql
├── dashboard/
│   └── bluestock_mf.pbix
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
└── README.md

---

## Features

### ETL & Data Processing

* Data ingestion and validation
* NAV data collection and processing
* Data cleaning and transformation
* Processed dataset generation

### Performance Analytics

* CAGR Analysis
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta
* Tracking Error
* Maximum Drawdown

### Advanced Analytics

* Value at Risk (VaR)
* Conditional VaR (CVaR)
* Rolling Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation Engine
* Sector Concentration Analysis (HHI)

### Dashboard Development

* Industry Overview Dashboard
* Fund Performance Dashboard
* Investor Analytics Dashboard
* SIP & Market Trends Dashboard

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd bluestock_mf_capstone
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib requests
```

---

## Running ETL Pipeline

Execute:

```bash
python run_pipeline.py
```

This script runs the available ETL and data-fetching modules sequentially.

---

## Running Individual Scripts

### Batch NAV Fetch

```bash
python scripts/batch_nav_fetch.py
```

### Live NAV Fetch

```bash
python scripts/live_nav_fetch.py
```

### Fund Recommender

```bash
python scripts/recommender.py
```

---

## Dashboard

The Power BI dashboard contains four pages:

1. Industry Overview
2. Fund Performance Analysis
3. Investor Analytics
4. SIP & Market Trends

### Opening the Dashboard

1. Open Power BI Desktop.
2. Open the project `.pbix` file.
3. Refresh the data if required.
4. Navigate through the dashboard pages using the page tabs.

---

## Key Outputs

* Performance Reports
* Risk Analytics Reports
* Investor Analytics Reports
* Power BI Dashboard
* Final Project Report
* Presentation Deck

---

## Author

**Arush Padmawar**

Bluestock Fintech Internship Project
