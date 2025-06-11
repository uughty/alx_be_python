class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance
       

 
    
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return True
        else:
            print("Deposit Must be positive amount.")
            return False
    
    def withdraw(self, amount):
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False
        
    def display_balance(self):
        print(f"Current balnce:{self._account_balance:.2f}")
        
    