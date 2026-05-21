import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
password = os.getenv("DB_PASSWORD")

def create_tables():
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="stock_tracker",
        user="postgres",
        password=password
) 
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_tracker(
                   unique_id SERIAL PRIMARY KEY,
                   stock_symbol TEXT NOT NULL,
                   company_name TEXT NOT NULL,
                   opening_price NUMERIC(10,2) NOT NULL,
                   closing_price NUMERIC(10,2) NOT NULL,
                   high_price NUMERIC(10,2) NOT NULL,
                   low_price NUMERIC(10,2) NOT NULL,
                   volume_traded INTEGER NOT NULL,
                   date_recorded TEXT NOT NULL
        )"""
    )

    connection.commit()
    connection.close()
    print("Table created successfully.")

if __name__ == "__main__":
    create_tables()
