class Account:
    def __init__(self, name, account_number, initial_balance=0):
        self.__name = name
        self.__account_number = account_number
        self.__balance = initial_balance
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount
        self.__transactions.append(f"Deposited: ${amount}")
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        self.__transactions.append(f"Withdrew: ${amount}")
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_transaction_history(self):
        return self.__transactions

    def get_account_info(self):
        return {
            "Name": self.__name,
            "Account Number": self.__account_number,
            "Balance": self.__balance
        }