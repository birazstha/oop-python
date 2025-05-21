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
        self.__transactions.append(f"Deposited: £{amount:.2f}")
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        self.__transactions.append(f"Withdrew: £{amount:.2f}")
        return self.__balance

    def getBalance(self):
        return self.__balance

    def getTransactionHistory(self):
        return self.__transactions

    def getAccountInfo(self):
        return {
            "Name": self.__name,
            "Account Number": self.__account_number,
            "Balance": self.__balance,
            "Account Type": "Standard"
        }

class SavingsAccount(Account):
    def __init__(self, name, account_number, initial_balance=0):
        super().__init__(name, account_number, initial_balance)
        self._Account__transactions.append("Created Savings Account")

    def getAccountInfo(self):
        """Override to include savings account type."""
        info = super().getAccountInfo()
        info["Account Type"] = "Savings"
        return info

class CheckingAccount(Account):
    def __init__(self, name, account_number, initial_balance=0):
        """Initialize a checking account, inheriting from Account."""
        super().__init__(name, account_number, initial_balance)
        self._Account__transactions.append("Created Checking Account")

    def getAccountInfo(self):
        """Override to include checking account type."""
        info = super().getAccountInfo()
        info["Account Type"] = "Checking"
        return info