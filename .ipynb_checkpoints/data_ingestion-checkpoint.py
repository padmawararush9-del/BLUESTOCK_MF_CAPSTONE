import pandas as pd
from pathlib import Path

# Folder containing the CSV files
DATA_DIR = Path("data/raw")

# List of datasets
files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 70)
print("TASK 3 - Loading all 10 CSV datasets")
print("=" * 70)

for file in files:

    file_path = DATA_DIR / file

    print("\n" + "-" * 60)
    print(f"Dataset: {file}")

    df = pd.read_csv(file_path)

    print(f"\nShape: {df.shape}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

print("\n" + "=" * 70)
print("All datasets loaded successfully")
print("=" * 70)
fund_master = pd.read_csv(DATA_DIR / "01_fund_master.csv")

print("\n" + "=" * 70)
print("TASK 6 - Fund Master Exploration")
print("=" * 70)

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())
nav_history = pd.read_csv(DATA_DIR / "02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("\n" + "=" * 70)
print("TASK 7 - AMFI Validation")
print("=" * 70)

print(f"Codes in Fund Master : {len(master_codes)}")
print(f"Codes in NAV History : {len(nav_codes)}")

if len(missing_codes) == 0:
    print("\nAll AMFI codes are present in nav_history")
else:
    print("\nMissing AMFI Codes:")
    print(missing_codes)