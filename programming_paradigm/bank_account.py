class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current balance: ${self.__account_balance:.2f}")



import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command> [amount]")
        print("Commands: create, deposit, withdraw, balance")
        sys.exit(1)

    command = sys.argv[1]

    try:
        account = BankAccount()
        account_file = "account_balance.txt"

        try:
            with open(account_file, "r") as file:
                account_balance = float(file.read())
                account = BankAccount(account_balance)
        except FileNotFoundError:
            pass

        if command == "create":
            account = BankAccount()
            with open(account_file, "w") as file:
                file.write(str(account_balance))
            account.display_balance()

        elif command == "deposit":
            if len(sys.argv) != 3:
                print("Usage: python main-0.py deposit <amount>")
                sys.exit(1)
            try:
                amount = float(sys.argv[2])
                if account.deposit(amount):
                    with open(account_file, "w") as file:
                        file.write(str(account._BankAccount__account_balance))
                    account.display_balance()
                else:
                    print("Invalid deposit amount.")
            except ValueError:
                print("Invalid amount.")

        elif command == "withdraw":
            if len(sys.argv) != 3:
                print("Usage: python main-0.py withdraw <amount>")
                sys.exit(1)
            try:
                amount = float(sys.argv[2])
                if account.withdraw(amount):
                    with open(account_file, "w") as file:
                        file.write(str(account._BankAccount__account_balance))
                    account.display_balance()
                else:
                    print("Insufficient funds or invalid withdrawal amount.")
            except ValueError:
                print("Invalid amount.")

        elif command == "balance":
            account.display_balance()

        else:
            print("Invalid command.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()