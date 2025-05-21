from bank import Bank

def main():
    bank = Bank()

    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Balance Inquiry")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter name: ")
                acc_num = input("Enter account number: ")
                balance = float(input("Enter initial deposit (£): "))
                print("Account types: 1. Standard 2. Savings")
                acc_type_choice = input("Choose account type (1-3): ")
                acc_type = "standard"
                if acc_type_choice == "2":
                    acc_type = "savings"
                elif acc_type_choice == "3":
                    acc_type = "checking"
                bank.createAccount(name, acc_num, balance, acc_type)
                print(f"Dear {name}, Your account has been created and your current balance is £{balance}")
            elif choice == "2":
                acc_num = input("Enter account number: ")
                account = bank.getAccount(acc_num)
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                print(f"Dear {name}, £{amount} has been deposited into your account.")
            elif choice == "3":
                acc_num = input("Enter account number: ")
                account = bank.getAccount(acc_num)
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
                print(f"Dear {name}, £{amount} has been withdrawn from your account.")

            elif choice == "4":
                acc_num = input("Enter account number: ")
                account = bank.getAccount(acc_num)
                print(f"Dear {name}, Your current balance is £{account.getBalance():.2f}")
            elif choice == "5":
                acc_num = input("Enter account number: ")
                account = bank.getAccount(acc_num)
                for t in account.getTransactionHistory():
                    print(t)
            elif choice == "6":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()