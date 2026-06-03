# Mutual Fund Analytics Capstone – Data Dictionary

## Overview

This document describes all datasets used in the Mutual Fund Analytics Capstone Project, including column definitions, data types, business meanings, and source references.

---

# 1. Fund Master Dataset

**File:** `clean_fund_master.csv`

**Source:** Internal Mutual Fund Master Data

| Column             | Data Type | Description                                  |
| ------------------ | --------- | -------------------------------------------- |
| amfi_code          | INTEGER   | Unique AMFI scheme identifier                |
| fund_house         | TEXT      | Asset Management Company (AMC) name          |
| scheme_name        | TEXT      | Mutual fund scheme name                      |
| category           | TEXT      | Scheme category (Equity, Debt, Hybrid, etc.) |
| sub_category       | TEXT      | Detailed scheme classification               |
| plan               | TEXT      | Direct or Regular plan                       |
| launch_date        | DATE      | Scheme launch date                           |
| benchmark          | TEXT      | Benchmark index                              |
| expense_ratio      | REAL      | Annual expense ratio (%)                     |
| exit_load          | REAL      | Exit load charged on redemption              |
| min_sip            | INTEGER   | Minimum SIP investment amount                |
| min_lumpsum        | INTEGER   | Minimum lump sum investment amount           |
| fund_manager       | TEXT      | Scheme fund manager                          |
| risk_grade         | TEXT      | Risk classification                          |
| amfi_category_code | TEXT      | Internal AMFI category code                  |

---

# 2. NAV History Dataset

**File:** `clean_nav.csv`

**Source:** MFAPI / AMFI NAV Data

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | INTEGER   | Scheme identifier |
| date      | DATE      | NAV date          |
| nav       | REAL      | Net Asset Value   |

---

# 3. Investor Transactions Dataset

**File:** `clean_transactions.csv`

**Source:** Simulated Investor Transaction Data

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Unique investor identifier |
| transaction_date   | DATE      | Transaction date           |
| amfi_code          | INTEGER   | Scheme identifier          |
| transaction_type   | TEXT      | SIP, Lumpsum, Redemption   |
| amount_inr         | REAL      | Transaction amount in INR  |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | Tier classification        |
| age_group          | TEXT      | Investor age bracket       |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | REAL      | Annual income in lakhs     |
| payment_mode       | TEXT      | Transaction payment method |
| kyc_status         | TEXT      | KYC verification status    |

---

# 4. Scheme Performance Dataset

**File:** `clean_performance.csv`

**Source:** Mutual Fund Performance Analytics

| Column             | Data Type | Description                         |
| ------------------ | --------- | ----------------------------------- |
| amfi_code          | INTEGER   | Scheme identifier                   |
| scheme_name        | TEXT      | Scheme name                         |
| fund_house         | TEXT      | AMC name                            |
| category           | TEXT      | Fund category                       |
| plan               | TEXT      | Direct or Regular                   |
| return_1yr_pct     | REAL      | One-year return (%)                 |
| return_3yr_pct     | REAL      | Three-year return (%)               |
| return_5yr_pct     | REAL      | Five-year return (%)                |
| benchmark_3yr_pct  | REAL      | Benchmark return (%)                |
| alpha              | REAL      | Alpha measure                       |
| beta               | REAL      | Beta measure                        |
| sharpe_ratio       | REAL      | Risk-adjusted return measure        |
| sortino_ratio      | REAL      | Downside risk-adjusted return       |
| std_dev_ann_pct    | REAL      | Annualized volatility               |
| max_drawdown_pct   | REAL      | Maximum drawdown (%)                |
| aum_crore          | REAL      | Assets Under Management (Crore INR) |
| expense_ratio_pct  | REAL      | Expense ratio (%)                   |
| morningstar_rating | INTEGER   | Morningstar rating                  |
| risk_grade         | TEXT      | Risk category                       |

---

# 5. AUM by Fund House Dataset

**File:** `clean_aum_by_fund_house.csv`

**Source:** Industry AUM Statistics

| Column         | Data Type | Description              |
| -------------- | --------- | ------------------------ |
| date           | DATE      | Reporting date           |
| fund_house     | TEXT      | AMC name                 |
| aum_lakh_crore | REAL      | AUM in lakh crores       |
| aum_crore      | REAL      | AUM in crores            |
| num_schemes    | INTEGER   | Number of active schemes |

---

# 6. Monthly SIP Inflows Dataset

**File:** `clean_monthly_sip_inflows.csv`

**Source:** Industry SIP Statistics

| Column                    | Data Type | Description                   |
| ------------------------- | --------- | ----------------------------- |
| month                     | DATE      | Reporting month               |
| sip_inflow_crore          | REAL      | Monthly SIP inflows           |
| active_sip_accounts_crore | REAL      | Active SIP accounts           |
| new_sip_accounts_lakh     | REAL      | New SIP registrations         |
| sip_aum_lakh_crore        | REAL      | SIP assets under management   |
| yoy_growth_pct            | REAL      | Year-over-Year SIP growth (%) |

---

# 7. Category Inflows Dataset

**File:** `clean_category_inflows.csv`

**Source:** Category-wise Industry Flows

| Column           | Data Type | Description                     |
| ---------------- | --------- | ------------------------------- |
| month            | DATE      | Reporting month                 |
| category         | TEXT      | Fund category                   |
| net_inflow_crore | REAL      | Net category inflow (Crore INR) |

---

# 8. Industry Folio Count Dataset

**File:** `clean_industry_folio_count.csv`

**Source:** Industry Folio Statistics

| Column              | Data Type | Description     |
| ------------------- | --------- | --------------- |
| month               | DATE      | Reporting month |
| total_folios_crore  | REAL      | Total folios    |
| equity_folios_crore | REAL      | Equity folios   |
| debt_folios_crore   | REAL      | Debt folios     |
| hybrid_folios_crore | REAL      | Hybrid folios   |
| others_folios_crore | REAL      | Other folios    |

---

# 9. Portfolio Holdings Dataset

**File:** `clean_portfolio_holdings.csv`

**Source:** Scheme Portfolio Disclosure Data

| Column            | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | INTEGER   | Scheme identifier        |
| stock_symbol      | TEXT      | NSE/BSE stock symbol     |
| stock_name        | TEXT      | Company name             |
| sector            | TEXT      | Business sector          |
| weight_pct        | REAL      | Portfolio weight (%)     |
| market_value_cr   | REAL      | Market value in crores   |
| current_price_inr | REAL      | Current market price     |
| portfolio_date    | DATE      | Portfolio reporting date |

---

# 10. Benchmark Indices Dataset

**File:** `clean_benchmark_indices.csv`

**Source:** NSE/BSE Benchmark Data

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | DATE      | Trading date         |
| index_name  | TEXT      | Benchmark index name |
| close_value | REAL      | Closing index value  |

---

## Database

**SQLite Database:** `data/bluestock_mf.db`

## Project Author

Mutual Fund Analytics Capstone Project – Bluestock Fintech Internship
