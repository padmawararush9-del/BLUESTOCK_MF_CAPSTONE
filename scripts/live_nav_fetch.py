import requests
import pandas as pd

print("=" * 60)
print("TASK 4 - LIVE NAV FETCH")
print("=" * 60)

# API URL
url = "https://api.mfapi.in/mf/125497"

# Fetch data
response = requests.get(url)

# Convert JSON
data = response.json()

# Show scheme details
print("\nScheme Information:")
print(data["meta"])

# Convert NAV history to DataFrame
df = pd.DataFrame(data["data"])

# Display first few rows
print("\nFirst 5 Records:")
print(df.head())

# Save CSV
csv_file = "data/raw/nav_125497.csv"
df.to_csv(csv_file, index=False)

print(f"\nCSV saved successfully: {csv_file}")
print(f"Total Records: {len(df)}")