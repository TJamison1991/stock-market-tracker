from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
from psycopg2.extras import RealDictCursor
password = os.getenv("DB_PASSWORD")

app = Flask (__name__)

@app.route("/api/stocks", methods=["GET"])
def get_stocks():
        connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="stock_tracker",
        user="postgres",
        password=password
    ) 
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM stock_tracker")
        stocks = [dict(row) for row in cursor.fetchall()]
        connection.close()
        return jsonify(stocks)

@app.route("/api/stocks/<symbol>", methods=["GET"])
def get_specific_stock(symbol):
        connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="stock_tracker",
        user="postgres",
        password=password
    )
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM stock_tracker WHERE stock_symbol = %s", (symbol,))
        row = cursor.fetchone()
        if row is None:
            return jsonify({"error": "Stock not found"}), 404
        stock = dict(row)
        connection.close()
        return jsonify(stock)

if __name__ == "__main__":
       app.run(debug=True)