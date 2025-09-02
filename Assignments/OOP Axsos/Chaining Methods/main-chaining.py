class User:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        print(f"Create Account, User Name: {self.name}, Account Balance: {self.balance}")
    
    def make_deposit(self, amount):
        self.balance += amount
        print(f"User Name: {self.name}, Make a deposit of {amount}")
        return self
    
    def make_withdrawal(self,amount):
        self.balance -=amount
        print(f"User {self.name} made a Withdrawal of {amount}")
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
        return self
    
    def transfer_money(self , other_account , amount):
        self.make_withdrawal(amount)
        other_account.make_deposit(amount)
        print(f"Transfer: ${amount} from: {self.name}, To: {other_account.name}")
        return self

# Add Users:
guido = User("Guido van Rossum", 250)
Jacob = User("Jacob Qumsiyeh", 750)


# For The Guido User:
guido.make_deposit(100).make_deposit(500).make_withdrawal(125.8).display_user_balance()
# For Jacob The User:
Jacob.make_deposit(1500).make_deposit(550).make_withdrawal(1500).transfer_money(guido , 150).display_user_balance()