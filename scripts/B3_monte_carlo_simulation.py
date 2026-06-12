from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent

nav = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_nav.csv"
)

fund_code = 100016

fund_nav = (
    nav[nav["amfi_code"] == fund_code]
    .sort_values("date")
)

returns = (
    fund_nav["nav"]
    .pct_change()
    .dropna()
)

mu = returns.mean()
sigma = returns.std()

current_nav = fund_nav["nav"].iloc[-1]

n_simulations = 1000
n_days = 252 * 5

simulations = np.zeros(
    (n_days, n_simulations)
)

for i in range(n_simulations):

    prices = [current_nav]

    for _ in range(n_days):

        daily_return = np.random.normal(
            mu,
            sigma
        )

        prices.append(
            prices[-1] * (1 + daily_return)
        )

    simulations[:, i] = prices[1:]

simulation_df = pd.DataFrame(simulations)

simulation_df.to_csv(
    BASE_DIR
    / "data"
    / "processed"
    / "monte_carlo_projection.csv",
    index=False
)

plt.figure(figsize=(12, 6))

plt.plot(
    simulations[:, :100],
    alpha=0.1
)

plt.title(
    f"Monte Carlo Simulation - Fund {fund_code}"
)

plt.xlabel("Trading Days")
plt.ylabel("Projected NAV")

plt.tight_layout()
plt.show()

print(
    "Monte Carlo simulation completed successfully."
)