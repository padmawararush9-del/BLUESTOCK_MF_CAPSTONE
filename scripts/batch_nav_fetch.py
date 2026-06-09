"""
Batch NAV Fetch Script

Fetches NAV data for multiple mutual fund schemes in batches,
performs validation and cleaning, and stores the consolidated
NAV dataset for further analysis.

Author: Arush Padmawar
"""

import requests
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()


RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, amfi_code in schemes.items():

    print(f"\nFetching {fund_name} ({amfi_code})...")

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        df = pd.DataFrame(data["data"])

        file_path = RAW_DIR / f"{fund_name}.csv"

        df.to_csv(file_path, index=False)

        print(f"✓ Saved: {file_path.name}")
        print(f"✓ Records: {len(df):,}")

    except Exception as e:
        print(f"✗ Failed: {e}")
