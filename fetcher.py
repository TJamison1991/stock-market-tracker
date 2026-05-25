import psycopg2
import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()
password = os.getenv("DB_PASSWORD")
api_key = os.getenv("ALPHA_VANTAGE_KEY")

symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

company_names = {
    "AAPL": "Apple Inc",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc",
    "AMZN": "Amazon.com Inc",
    "TSLA": "Tesla Inc"
}

def fetch_stocks():
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="stock_tracker",
        user="postgres",
        password=password
    ) 
    cursor = connection.cursor()
    for symbol in symbols:
        company = company_names[symbol]
        api_url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
        response = requests.get(api_url)
        data = response.json()
        quote = data["Global Quote"]
        symbol_val = quote["01. symbol"]
        open_price = quote["02. open"]
        high = quote["03. high"]
        low = quote["04. low"]
        close = quote["05. price"]
        volume = quote["06. volume"]
        date = quote["07. latest trading day"]
        cursor.execute("""
            INSERT INTO stock_tracker(
                stock_symbol, company_name, opening_price,
                closing_price, high_price, low_price,
                volume_traded, date_recorded)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (symbol_val, company, open_price, close, high, low, volume, date))
        print(f"{symbol} data loaded successfully.")
        time.sleep(15)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    fetch_stocks()