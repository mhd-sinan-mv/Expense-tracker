
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "expense_tracker.db"


def initialize_database():

    connection = sqlite3.connect(DB_PATH)

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount INTEGER NOT NULL,
                category TEXT NOT NULL,
                transaction_type TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                month TEXT NOT NULL,
                limit_amount INTEGER NOT NULL,
                UNIQUE(category, month) 
            )
        """)#unique ensures that each category can have only one budget per month

        connection.commit()

    finally:
        connection.close()
