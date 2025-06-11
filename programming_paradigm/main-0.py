import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # starting balance for example

    if len(sys.argv) < 2:
        print("Usage: python main-0.py [deposit|withdraw|balance] [amount]")
        return

    command = sys.argv[1].lower()

    if command == "deposit" and len(sys.argv) == 3:
        amount = float(sys.argv[2])
        account.deposit(amount)
        account.display_balance()

    elif command == "withdraw" and len(sys.argv) == 3:
        amount = float(sys.argv[2])
        success = account.withdraw(amount)
        if success:
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")
        account.display_balance()

    elif command == "balance":
        account.display_balance()

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
