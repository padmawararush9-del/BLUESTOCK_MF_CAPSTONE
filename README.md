# Mutual Fund Analytics Project

> End-to-end data pipeline and analytics suite for Indian mutual fund data.

## Project Structure

```
mf_analysis/
├── data/
│   ├── raw/               # Source CSVs, JSON from AMFI / mfapi.in
│   └── processed/         # Cleaned, validated, enriched data
├── notebooks/             # Jupyter exploration notebooks
├── sql/                   # SQL queries & schema definitions
├── dashboard/             # Plotly / Dash dashboard code
├── reports/               # Auto-generated PDF / HTML reports
├── data_ingestion.py      # Day 1 – Load, inspect, validate all 10 CSVs
├── live_nav_fetch.py      # Day 1 – Live NAV fetch from mfapi.in
└── requirements.txt
```

## Day 1 Datasets (data/raw/)

| # | File | Rows | Description |
|---|------|------|-------------|
| 1 | fund_master.csv | 21 | AMFI scheme master (codes, categories, AUM) |
| 2 | nav_history.csv | 20,076 | Daily NAV Jan 2020 – May 2026 |
| 3 | scheme_categories.csv | 22 | SEBI category taxonomy |
| 4 | aum_monthly.csv | 462 | Month-end AUM per scheme |
| 5 | top_holdings.csv | 90 | Portfolio holdings per fund |
| 6 | sip_performance.csv | 120 | SIP returns at various tenures |
| 7 | fund_returns.csv | 42 | Point-to-point returns vs benchmark |
| 8 | risk_metrics.csv | 6 | Sharpe, Sortino, Beta, max-drawdown |
| 9 | benchmark_comparison.csv | 8,365 | Nifty 50/100/200, Sensex index values |
| 10 | expense_ratios.csv | 21 | Direct vs regular plan TER |

## Quick Start

```bash
pip install -r requirements.txt
python data_ingestion.py    # Tasks 3, 6, 7
python live_nav_fetch.py    # Tasks 4, 5
```

## API Source

Live NAV data: [mfapi.in](https://www.mfapi.in)  
`GET https://api.mfapi.in/mf/{amfi_code}`

## Key Schemes Tracked

| AMFI Code | Scheme |
|-----------|--------|
| 125497 | HDFC Top 100 Fund Direct Growth |
| 119551 | SBI Bluechip Fund Direct Growth |
| 120503 | ICICI Prudential Bluechip Fund Direct Growth |
| 118632 | Nippon India Large Cap Fund Direct Growth |
| 119092 | Axis Bluechip Fund Direct Growth |
| 120841 | Kotak Bluechip Fund Direct Growth |
