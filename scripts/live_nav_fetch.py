import requests
import pandas as pd

print("=" * 60)
print("TASK 4 - LIVE NAV FETCH")
print("=" * 60)


url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print("\nScheme Information:")
print(data["meta"])

df = pd.DataFrame(data["data"])

print("\nFirst 5 Records:")
print(df.head())

csv_file = "data/raw/nav_125497.csv"
df.to_csv(csv_file, index=False)

print(f"\nCSV saved successfully: {csv_file}")
print(f"Total Records: {len(df)}")