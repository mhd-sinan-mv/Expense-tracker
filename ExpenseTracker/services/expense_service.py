
import sqlite3

from database.db import DB_PATH
from models.transaction import Transaction


def add_transaction(transaction: Transaction):

    connection = sqlite3.connect(DB_PATH)

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO transactions
            (amount, category, transaction_type, date, description)
            VALUES (?, ?, ?, ?, ?)
        """, (
            transaction.amount,
            transaction.category,
            transaction.transaction_type,
            transaction.date,
            transaction.description
        ))

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()

def get_all_transactions():

    connection = sqlite3.connect(DB_PATH)

    try:
        cursor = connection.cursor()

        cursor.execute("""SELECT id , amount, category, transaction_type, date, description FROM transactions ORDER BY date ASC , id ASC""") #fetches all the transactions from the database and orders them by date in descending order and then by id in descending order
        rows = cursor.fetchall()

        transactions = []
        for row in rows:
            transaction = Transaction(
                transaction_id=row[0],
                amount=row[1],
                category=row[2],
                transaction_type=row[3],
                date=row[4],
                description=row[5]
            )
            transactions.append(transaction) #Adds each newly created Transaction object to our list.

        return transactions

    finally:
        connection.close()


def display_transactions():

    transactions = get_all_transactions()

    if not transactions:
        print("\nNo transactions found.")
        return

    print("\n" + "=" * 75)
    print("TRANSACTION HISTORY")
    print("=" * 75)

    print(
        f"{'ID':<5}"
        f"{'CATEGORY':<15}"
        f"{'TYPE':<12}"
        f"{'AMOUNT':<15}"
        f"{'DATE':<15}"  
        # <15 means left-align the text within 15 characters.
        # <12 means left-align within 12 characters.
        # .2f means display two decimal places.
    )

    print("-" * 75)

    for transaction in transactions:

        amount = transaction.amount / 100

        print(
            f"{transaction.id:<5}"
            f"{transaction.category:<15}"
            f"{transaction.transaction_type:<12}"
            f"₹{amount:<14.2f}"
            f"{transaction.date:<15}"
        )

    print("=" * 75)
