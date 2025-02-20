import requests
import os

# Load API key from environment variable or set it manually
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = "https://www.alphavantage.co/query"


def fetch_stock_data(symbol):
    params = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "apikey": API_KEY}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print("✅ API Response Received!")
        return data
    else:
        print(f"❌ API Request Failed: {response.status_code}")
        print(response.text)
        return None


if __name__ == "__main__":
    stock_data = fetch_stock_data("QBTS")
    if stock_data:
        print(stock_data)
