class User:
    def __init__(self,name,int_rate =.01,balance=0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
    
    def make_withdrawal(self,amount):
        if self.balance - amount > 0:
            self.balance -= amount;
        else:
            self.balance -= 5;
            print("Insufficient funds: Charging a $5 fee")
    
    def deposit(self,amount):
        self.balance += amount

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        self.balance += self.balance * .01

    def transfer_money(self,amount,account):
        if self.balance - amount > 0:
            self.balance -= amount;
            account.deposit(amount)
        else:
            self.balance -= 5;
            print("Insufficient funds: Charging a $5 fee")

lisa = User("lisa")
lisa.deposit(100)
lisa.deposit(50)
lisa.deposit(250)
lisa.make_withdrawal(20)
lisa.yield_interest()
lisa.display_account_info()

natalie = User("natalie")
natalie.deposit(5000)
natalie.deposit(3500)
natalie.make_withdrawal(250)
natalie.make_withdrawal(500)
natalie.make_withdrawal(1500)
natalie.make_withdrawal(1200)
natalie.yield_interest()
natalie.display_account_info()
