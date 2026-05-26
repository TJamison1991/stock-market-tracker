# STOCK MARKET TRACKER

This project is meant to act as a stock tracker api that highlights the full understanding and use of PostgreSQL. This project contains contains a PostgreSQL table called stock_tracker that holds data pulled from Alpha Vantage API.

## Features
- Fetch live stock data from Alpha Vantage API
- Store stock data in PostgreSQL database
- Serve stock data through a REST API
- Filter by stock symbol

## Project Structure
```
stock-market-tracker/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
├── fetcher.py
│
├── data/

```
## How To Install And Run
- Clone the repo from GitHub
    git clone <repository-url>
- Navigate to stock-market-tracker
- Install dependencies
    pip install -r requirements.txt
- Create a .env file with:
    DB_PASSWORD=your_postgres_password
    ALPHA_VANTAGE_KEY=your_api_key
- Set up the database
    python database.py
- Seed the database
    python fetcher.py
- Run the app
    python app.py

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | /api/stocks | Returns all stocks |
| GET | /api/stocks/<symbol> | Returns single stock |

## Technologies Used
- Python 3
- Flask - web framework
- PostgreSQL - database storage
- JSON - data format for API responses
- Alpha Vantage - Live API stock tracker

## What I Learned
I learned how to build a live stock tracker that stores data inside a PostgreSQL table. Using PostgreSQL for this project specifically instead of SQLite helps me understand how the real world operates. I specifically used PostgreSQL to strengthen my knowledge of how to connect and navigate a table using DBeaver. Because I'm using PostgreSQL, I also used psycopg2, which I used frequently in my previous job to connect to the database. I also learned how to use RealDictCursor to loop through my dictionaries in app.py. Throughout this project, I also learned how to better set up a repo structure to help myself remain organized. When creating the live stock tracker, I learned how to create and store data inside a PostgreSQL table called stock_tracker. If I continued on with this, I would like to add more data to the table. Maybe even personalize it more to track stocks that I actually invest in. 