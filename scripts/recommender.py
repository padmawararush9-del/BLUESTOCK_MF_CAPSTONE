"""
Fund Recommendation Engine

Recommends the top mutual funds based on investor
risk appetite and Sharpe Ratio rankings.

Author: Arush Padmawar
"""

import pandas as pd

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

funds = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_performance.csv"
)

risk_appetite = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

recommendation_table = (
    funds[
        funds["risk_grade"].str.lower()
        == risk_appetite.lower()
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
    [
        [
            "amfi_code",
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)

print("\nTop 3 Recommended Funds:\n")
print(recommendation_table.to_string(index=False))