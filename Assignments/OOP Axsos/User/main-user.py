class User:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        print(f"Create Account, User Name: {self.name}, Account Balance: {self.balance}")
    
    def make_deposit(self, amount):
        self.balance += amount
        print(f"User Name: {self.name}, Make a deposit of {amount}")
    
    def make_withdrawal(self,amount):
        self.balance -=amount
        print(f"User {self.name} made a Withdrawal of {amount}")
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")


# Add Users:
guido = User("Guido van Rossum", 250)
Jacob = User("Jacob Qumsiyeh", 750)

# For The Guido User:
guido.make_deposit(100)
guido.make_deposit(63.9)
guido.make_deposit(14.2)
guido.make_withdrawal(120.5)
guido.display_user_balance()

# For Jacob The User:
Jacob.make_deposit(1500)
Jacob.make_deposit(550)
Jacob.make_withdrawal(1500)
Jacob.display_user_balance()