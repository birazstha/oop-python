from account import Account, SavingsAccount, CheckingAccount

class Bank:
    def __init__(self):
        self.accounts = {}

    def createAccount(self, name, account_number, initial_balance=0, account_type="standard"):
        if account_number in self.accounts:
            raise ValueError("Account number already exists. Please enter the new one.")
        if account_type.lower() == "savings":
            self.accounts[account_number] = SavingsAccount(name, account_number, initial_balance)
        elif account_type.lower() == "checking":
            self.accounts[account_number] = CheckingAccount(name, account_number, initial_balance)
        else:
            self.accounts[account_number] = Account(name, account_number, initial_balance)

    def getAccount(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number]