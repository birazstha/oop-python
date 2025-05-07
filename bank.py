from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number, initial_balance=0):
        if account_number in self.accounts:
            raise ValueError("Account number already exists.")
        self.accounts[account_number] = Account(name, account_number, initial_balance)

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number]