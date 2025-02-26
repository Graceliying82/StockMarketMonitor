import requests
from database import SessionLocal, engine
from models import Stock
from sqlalchemy.orm import sessionmaker
import json
import os

ALPHA_VANTAGE_URI = "https://www.alphavantage.co/query"
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

def fetch_stock_data(symbol="TSLA"):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": ALPHA_VANTAGE_KEY,
    }

    response = requests.get(ALPHA_VANTAGE_URI, params= params)

    data = response.json()

    print(json.dumps(data, indent=4))

    # Get the latest timestamp from the data
    latest_time = list(data["Time Series (5min)"].keys())[0]
    details = data["Time Series (5min)"][latest_time]
    # Start a session
    session = SessionLocal()
    stock = Stock(symbol=symbol, price=float(details["1. open"]), volume=int(details["5. volume"]))
    session.add(stock)
    session.commit()
    session.close()

    print(f"Stored {symbol} data in DB")

if __name__ == "__main__":
    fetch_stock_data()