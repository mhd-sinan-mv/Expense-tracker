from decimal import Decimal, InvalidOperation
from webbrowser import get

from database.db import initialize_database
from models.transaction import Transaction
from datetime import date, datetime
from decimal import Decimal,InvalidOperation
from services.expense_service import *
initialize_database()
# print("Database inititalized succesfully") commented because it is already initialized

# t1=Transaction(100, "Food", "Expense", "2023-10-01", "Lunch at restaurant")
# t1.display() #method calling
# print(t1) #str calling , both display the same output but in different format

def get_amount_in_paise(): #since decimal is not supported in sqlite , we convert rupees into paise and store it as int

    try:
        amount = Decimal(input("Enter amount in rupees: "))

        if not amount.is_finite() or amount <= 0:
            raise ValueError("Amount must be positive")

        paise = amount * 100

        if paise != paise.to_integral_value():
            raise ValueError("Maximum two decimal places allowed")

        return int(paise)

    except InvalidOperation:
        raise ValueError("Enter a valid numeric amount")

def get_amount_in_paise_updation():
    try:
        amount = Decimal(input("Enter amount in rupees: "))
        paise = amount * 100

        if paise > 0:
            return int(paise)
        else:
            return None
    except:
        return None

def main():

    initialize_database()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:

                transaction_type = input(
                    "Enter type (income/expense/): "
                ).strip().lower()

                amount = get_amount_in_paise()

                category = input("Enter category: ")

                transaction_date = input(
                    "Enter date (YYYY-MM-DD), or press Enter for today: "
                ).strip()

                if not transaction_date:
                    transaction_date = date.today().isoformat()

                description = input("Enter description: ")

                transaction = Transaction(
                    amount=amount,
                    category=category,
                    transaction_type=transaction_type,
                    date=transaction_date,
                    description=description
                ) #takes input as object of Transaction class and stores in transaction variable

                transaction_id = add_transaction(transaction) #passes the transaction object to add_transaction function and stores the returned value in transaction_id variable to push the data to database

                print("\nTransaction saved successfully!")
                print("Transaction ID:", transaction.id)
                print(transaction)

            except ValueError as error:
                print("Invalid input:", error)
        elif choice == "2":

            display_transactions()

        elif choice == "3":
            display_transactions()

            try:
                transaction_id = int(input("\nEnter transaction ID to update: "))

                old = get_transaction_by_id(transaction_id)

                amount = get_amount_in_paise_updation()
                if not amount:
                    amount = old.amount

                category = input("Enter new category: ").strip()
                if not category:
                    category = old.category
            
                transaction_type = input(
                    "Enter type (income/expense): "
                ).strip().lower()
                if not transaction_type:
                    transaction_type = old.transaction_type

                transaction_date = input(
                    "Enter new date (YYYY-MM-DD): or press Enter for today: "
                ).strip()
                if not transaction_date:
                    transaction_date = date.today().isoformat()

                description = input("Enter new description: ").strip()
                if not description:
                    description = old.description

                # Validate the new values by creating a Transaction object
                transaction = Transaction(
                    transaction_id=transaction_id,
                    amount=amount,
                    category=category,
                    transaction_type=transaction_type,
                    date=transaction_date,
                    description=description
                )

                result = update_transaction(
                    transaction.id,
                    transaction.amount,
                    transaction.category,
                    transaction.transaction_type,
                    transaction.date,
                    transaction.description
                )

                if result:
                    print("\nTransaction updated successfully!")
                else:
                    print("\nNo transaction found with that ID.")

            except ValueError as error:
                print("Invalid input:", error)

        elif choice == "4":
            display_transactions()
            try:
                    transaction_id = int(input("\nEnter transaction ID to update: "))
                    confirmation = input("Are you sure you want to delete it? (yes/no): ").strip().lower()
                    if confirmation == "yes":
                        result = delete_transaction(transaction_id)
                        if result:
                            print("\nTransaction deleted successfully!")
                        else:
                            print("\nNo transaction found with that ID.")
            except ValueError as error:
                    print("Invalid input:", error)

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__": #This ensures main() runs when you execute main.py directly, but not when another Python file imports it.
    main() 


from decimal import Decimal, InvalidOperation



