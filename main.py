from bank import Bank

def main():
    bank = Bank()

    while True:
        
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter name: ")
                acc_num = input("Enter account number: ")
                balance = float(input("Enter initial deposit: "))
                bank.create_account(name, acc_num, balance)
                print("Account created.")
            elif choice == "2":
                acc_num = input("Enter account number: ")
                amount = float(input("Enter amount to deposit: "))
                account = bank.get_account(acc_num)
                account.deposit(amount)
                print("Deposit successful.")
            elif choice == "3":
                acc_num = input("Enter account number: ")
                amount = float(input("Enter amount to withdraw: "))
                account = bank.get_account(acc_num)
                account.withdraw(amount)
                print("Withdrawal successful.")
            elif choice == "4":
                acc_num = input("Enter account number: ")
                account = bank.get_account(acc_num)
                print(f"Balance: ${account.get_balance()}")
            elif choice == "5":
                acc_num = input("Enter account number: ")
                account = bank.get_account(acc_num)
                for t in account.get_transaction_history():
                    print(t)
            elif choice == "6":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()