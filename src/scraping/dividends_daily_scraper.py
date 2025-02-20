import requests
import pandas as pd
import json
import uuid
from datetime import datetime, UTC
from io import StringIO  # ✅ Fix for FutureWarning

# Set the URL
url = "https://www.investing.com/dividends-calendar/"

# Fake User-Agent (mimics a real browser)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Fetch the page
response = requests.get(url, headers=headers, timeout=10)

if response.status_code == 200:
    # ✅ Wrap HTML response in StringIO to avoid FutureWarning
    html_io = StringIO(response.text)
    dfs = pd.read_html(html_io)

    if len(dfs) > 0:
        df = dfs[0]  # Get the first table

        # 🛠 Drop the first row (which contains extra headers)
        df = df.iloc[1:].reset_index(drop=True)

        # 🛠 Fix multi-index column headers
        df.columns = (
            df.columns.droplevel(0)
            if isinstance(df.columns, pd.MultiIndex)
            else df.columns
        )

        # 🛠 Rename columns
        df.columns = [
            "placeholder",
            "Company",
            "Ex-Dividend Date",
            "Dividend",
            "Type",
            "Payment Date",
            "Yield",
        ]

        # 🛠 Drop NaN values in "Company" column
        df = df[df["Company"].notna()]

        # 🛠 Clean whitespace
        df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

        # 🛠 Reset index
        df.reset_index(drop=True, inplace=True)

        # ✅ Generate metadata
        metadata = {
            "column_names": df.columns.tolist(),
            "dtypes": df.dtypes.astype(str).to_dict(),
        }

        # ✅ Save each row as a JSON object
        json_records = []
        for _, row in df.iterrows():
            record = {
                "id": str(uuid.uuid4()),  # Generate unique ID
                "sourcename": "investing.com_dividends",
                "uploaded_at": datetime.now(UTC).isoformat(),
                "raw_data": json.dumps({"metadata": metadata, "data": row.to_dict()}),
            }
            json_records.append(record)

        # ✅ Generate timestamped filename
        timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
        json_filename = f"scraping_investorcom_dividends_{timestamp}.json"

        # ✅ Save JSON file with timestamped name
        with open(json_filename, "w") as f:
            json.dump(json_records, f, indent=4)

        print(f"✅ Saved {len(json_records)} records to {json_filename}")

    else:
        print("⚠️ No tables found in HTML response.")
else:
    print(f"❌ Error {response.status_code}: Access denied.")
