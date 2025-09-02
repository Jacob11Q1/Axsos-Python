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

# Add Users:
Jacob = BankAccount(int_rate = 0.01 , balance = 100)
Jacob.deposit(150).deposit(80).deposit(25).withdraw(350).yield_interest().display_account_info("Jacob Qumsiyeh")

Hani = BankAccount(int_rate = 0.01 , balance = 150)
Hani.deposit(150).deposit(200).withdraw(100).withdraw(50).withdraw(65).withdraw(100).yield_interest().display_account_info("Hani Abdo")
