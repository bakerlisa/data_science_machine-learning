class BankAccount:
    def __init__(self,name,int_rate=0.01,balance=0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insuffienct funds")

    def withdraw(self,amount):
        self.balance += amount

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        self.balance += self.balance*int_rate
