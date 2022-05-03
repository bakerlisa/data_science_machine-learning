class BankAccount:
    def __init__(self,int_rate=0.01,balance=0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insuffienct funds")
        
    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        self.balance += self.balance*int_rate


