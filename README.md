# Mutual Fund Analytics Capstone

## Overview

This project is being developed as part of the Bluestock Fintech Data Analytics Internship. The objective is to build an end-to-end Mutual Fund Analytics platform using Python, SQL, SQLite, and Power BI.

The project covers data ingestion, cleaning, database design, analytics, performance evaluation, and dashboard development.

---

## Project Objectives

* Collect and ingest mutual fund datasets
* Clean and validate financial data
* Build a SQLite analytical database
* Perform SQL-based analytics
* Generate fund performance insights
* Build interactive Power BI dashboards
* Develop advanced analytics and recommendation systems

---

## Project Structure

```text
bluestock_mf_capstone/

├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│       └── bluestock_mf.db

├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_sql_analysis.ipynb

├── scripts/
│   └── live_nav_fetch.py

├── sql/
│   ├── schema.sql
│   └── queries.sql

├── reports/
│   └── data_dictionary.md

└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQLAlchemy
* Jupyter Notebook
* Git & GitHub
* Power BI (Upcoming)

---

## Day 1 Deliverables

* Data ingestion pipeline
* Mutual fund master dataset
* Historical NAV dataset
* Live NAV fetch using MFAPI
* Data validation reports

---

## Day 2 Deliverables

### Data Cleaning

* Fund Master
* NAV History
* Investor Transactions
* Scheme Performance
* AUM by Fund House
* Monthly SIP Inflows
* Category Inflows
* Industry Folio Counts
* Portfolio Holdings
* Benchmark Indices

### Database

* SQLite Star Schema Design
* Dimension and Fact Tables
* Database Loading using SQLAlchemy
* Row Count Validation

### Analytics

* 10 Analytical SQL Queries
* SIP YoY Growth Analysis
* Fund Performance Analysis

### Documentation

* Data Dictionary
* SQL Schema Documentation

---

## Current Database Tables

* dim_fund
* fact_nav
* fact_transactions
* fact_performance
* fact_aum
* fact_sip_inflows
* fact_category_inflows
* fact_industry_folios
* fact_portfolio_holdings
* fact_benchmark_indices

---
## EDA & Analytics Completed

### Exploratory Data Analysis

Performed detailed exploratory data analysis on mutual fund datasets covering NAV trends, AUM growth, SIP inflows, investor demographics, folio growth, and portfolio allocations.

### Key Visualizations Created

* NAV Trend Analysis (2022–2026)
* Average NAV Trend with 2023 Bull Run and 2024 Market Correction
* AUM Growth by Fund House
* Monthly SIP Inflow Trend
* Category-wise Inflow Heatmap
* Investor Age Group Distribution
* SIP Amount Distribution by Age Group
* Gender Distribution of Investors
* SIP Amount by State
* T30 vs B30 Investor Distribution
* Mutual Fund Folio Growth
* NAV Return Correlation Matrix
* Sector Allocation Donut Chart
* Folio Growth by Category
* Active SIP Accounts Growth

### Key Insights

* Mutual fund NAVs showed consistent long-term growth.
* SIP inflows reached a record ₹31,002 Cr in December 2025.
* SBI Mutual Fund remained the largest fund house by AUM.
* Investors aged 26–35 formed the largest investor segment.
* Mutual fund folios grew from 13.26 Cr to 26.12 Cr between 2022 and 2025.
* T30 cities accounted for the majority of investors.
* Equity folios grew significantly faster than debt and hybrid folios.

### Deliverables

* 10 Cleaned Datasets
* SQLite Database (`bluestock_mf.db`)
* SQL Schema and Analytical Queries
* Data Dictionary Documentation
* 15 EDA Visualizations
* EDA Findings Documentation
* Jupyter Notebooks for Analysis


---

## Author

Arush Padmawar

Bluestock Fintech Internship – Mutual Fund Analytics Capstone
