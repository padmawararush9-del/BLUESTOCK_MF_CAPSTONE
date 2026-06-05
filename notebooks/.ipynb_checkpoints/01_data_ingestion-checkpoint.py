import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")

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
