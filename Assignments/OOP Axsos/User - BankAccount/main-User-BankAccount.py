# Bank Account Assignment:
class BankAccount:
    def __init__(self, int_rate , balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self , amount):
        self.balance += amount
        return self
    
    def withdraw(self , amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self , name = ""):
        print(f"{name} - Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
            print(f"Interest added: ${interest: .2f}")
        else:
            print("No interest added. Balance is non-positive")
        return self


# Class User:
class User:
    def __init__(self, name, int_rate = 0.01 , starting_balance = 0):
        self.name = name
        self.account = BankAccount(int_rate , starting_balance)
        print(f"Create Account, User Name: {self.name}, Account Balance: {self.account.balance}")

    def display_All_Info(self):
        print(f"User: {self.name}")
        print(f"Account Balance: ${self.account.balance}")
        print(f"Ineterst Rate: {self.account.int_rate:100.2f}%")
        print("---------------------------------")


# Add Users:
guido = User("Guido Van Rossum" , int_rate = 0.02, starting_balance = 150)
guido.account.deposit(100).deposit(50).withdraw(150).yield_interest().display_account_info()

jacob = User("Jacob Qumsiyeh" , int_rate = 0.02 , starting_balance = 250)
jacob.account.deposit(250).deposit(150).deposit(200).withdraw(500).yield_interest().display_account_info()
