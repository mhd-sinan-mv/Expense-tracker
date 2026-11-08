from datetime import datetime

class Transaction:

    def __init__(self, amount:float, category:str, transaction_type:str, date:str, description:str="",transaction_id: int | None = None): #Why add transaction_id? When we create a new transaction, SQLite generates its ID. When we retrieve an existing transaction, we need to retain that ID so we can later update or delete that particular record.The int | None type hint means the ID can be an integer or None.

        if amount <= 0: #validation for amount
            raise ValueError("Amount must be greater than zero.")
        if transaction_type not in ["Income", "Expense", "income", "expense"]:#validation for transaction type
            raise ValueError("Transaction type must be either 'Income' or 'Expense'.")
        if not category.strip():#validation for category
            raise ValueError("Category cannot be empty.")
        datetime.strptime(date, "%Y-%m-%d") # Validate date format

        self.id = transaction_id
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.date = date
        self.description = description

    def __str__(self):
        return f"{self.date} - {self.category}: ₹{self.amount/100} - {self.description}"

    def display(self):
        print(f"Date: {self.date}")
        print(f"Category: {self.category}")
        print(f"Amount: ₹{self.amount/100}") #because amount is stored in paise, we convert it back to rupees for display
        print(f"Type: {self.transaction_type}")
        print(f"Description: {self.description}")
        