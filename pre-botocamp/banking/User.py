class User:
    def __init__(self,name,account=0):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_withdrawal(self,amount):
        if(self.account - amount >= 0):
            self.account -= amount
        else:
            print("Insufficicent funds")
    
    def make_deposit(self,amount):
        self.account += amount
    
    def display_user_balance(self):
        print(f"Balance: ${self.account}")

    def transfer_money(self,amount,account):
        if(self.account - amount >= 0):
            self.account - amount
            account.make_deposit(amount)
        else:
            print("Insufficicent funds")

lisa = User("lisa",500)
lisa.make_withdrawal(200)
lisa.make_deposit(100)
lisa.display_user_balance()

natalie = User("natalie",200)
natalie.make_withdrawal(100)
natalie.make_deposit(200)
natalie.display_user_balance()