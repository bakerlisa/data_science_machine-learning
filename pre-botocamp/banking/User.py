class User:
    def __init__(self,name,account):
        self.name = name
        self.account = account
    
    def make_withdrawal(self,amount):
        if(self.account - amount > 0):
            self.account - amount
        else:
            print("Insufficicent funds")
    
    def make_deposit(self,amount):
        self.account += amount
    
    def display_user_balance(self)
        print(f"Balance: ${account}")

    def transfer_money(self,amount,account)
        if(self.account - amount > 0):
            self.account - amount
            account.make_deposit(amount)
        else:
            print("Insufficicent funds")