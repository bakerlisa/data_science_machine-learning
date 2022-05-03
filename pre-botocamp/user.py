class User:
    def __init__(self, name,account_balance=0):
        self.name = name
        self.account_balance = account_balance
    
    def make_withdrawal(self,amount):
        if self.account_balance - amount > 0:
            self.account_balance -= amount;
        else:
            print("you don't have enough funds")
    
    def make_deposit(self,amount):
        self.account_balance += amount;

    def display_user_balance(self):
        print(f"User {self.name} has a balance of: ${self.account_balance}")

    def transfer_money(self,amount,account):
        if self.account_balance - amount > 0:
            self.account_balance -= amount
            account.make_deposit(amount)
        else:
            print("Insufficent funds")

natalie = User("Natalie",600)
lisa = User("Lisa",500)
lisa.make_withdrawal(100)

lisa.transfer_money(100,natalie)
lisa.display_user_balance()
natalie.display_user_balance()
