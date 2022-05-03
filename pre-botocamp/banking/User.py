from BankAccount import BankAccount

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02,balance=0)
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
    
    def make_deposit(self,amount):
        self.account.deposit(amount)
    
    def display_user_balance(self):
        self.account.display_account_info()

    def transfer_money(self,amount,account):
        self.account.withdraw(amount)
        if(self.account.balance <= 0):
            account.account.deposit(amount)

lisa = User("lisa","lisa@lisa.com")
lisa.make_deposit(500)
# lisa.make_withdrawal(200)


natalie = User("natalie","nat@nat.com")

lisa.transfer_money(500,natalie)
lisa.display_user_balance()
natalie.display_user_balance()