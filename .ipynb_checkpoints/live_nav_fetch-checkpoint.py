{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "98f35b54-f0d6-4ea3-bea4-340a630479ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "============================================================\n",
      "TASK 4 - LIVE NAV FETCH\n",
      "============================================================\n",
      "\n",
      "Scheme Information:\n",
      "{'fund_house': 'SBI Mutual Fund', 'scheme_type': 'Open Ended Schemes', 'scheme_category': 'Equity Scheme - Small Cap Fund', 'scheme_code': 125497, 'scheme_name': 'SBI Small Cap Fund - Direct Plan - Growth', 'isin_growth': 'INF200K01T51', 'isin_div_reinvestment': None}\n",
      "\n",
      "First 5 Records:\n",
      "         date        nav\n",
      "0  01-06-2026  192.31950\n",
      "1  31-05-2026  193.68360\n",
      "2  29-05-2026  193.68480\n",
      "3  27-05-2026  195.05010\n",
      "4  26-05-2026  194.22580\n",
      "\n",
      "CSV saved successfully: data/raw/nav_125497.csv\n",
      "Total Records: 3091\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "print(\"=\" * 60)\n",
    "print(\"TASK 4 - LIVE NAV FETCH\")\n",
    "print(\"=\" * 60)\n",
    "\n",
    "# API URL\n",
    "url = \"https://api.mfapi.in/mf/125497\"\n",
    "\n",
    "# Fetch data\n",
    "response = requests.get(url)\n",
    "\n",
    "# Convert JSON\n",
    "data = response.json()\n",
    "\n",
    "# Show scheme details\n",
    "print(\"\\nScheme Information:\")\n",
    "print(data[\"meta\"])\n",
    "\n",
    "# Convert NAV history to DataFrame\n",
    "df = pd.DataFrame(data[\"data\"])\n",
    "\n",
    "# Display first few rows\n",
    "print(\"\\nFirst 5 Records:\")\n",
    "print(df.head())\n",
    "\n",
    "# Save CSV\n",
    "csv_file = \"data/raw/nav_125497.csv\"\n",
    "df.to_csv(csv_file, index=False)\n",
    "\n",
    "print(f\"\\nCSV saved successfully: {csv_file}\")\n",
    "print(f\"Total Records: {len(df)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f857d98a-c6a4-49e3-8d05-31c0f069bbd9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
