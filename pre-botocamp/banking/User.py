class User:
    def __init__(self,name,amount=0):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=amount)
    
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


natalie = User("natalie",200)
