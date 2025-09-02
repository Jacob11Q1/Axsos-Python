# Attributes: get familiar with the __init__() method

class user():
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdoho.com"
        self.account_balance = 0
guido = user()
monty = user()
# How to access the Attributes
print(guido.name) # Output: Miachael
print(monty.name) # Output: Miachael

# We can also set the values for our instance's attributes:
guido.name = "Guido"
monty.name = "Monty"

# Another Example Of The Class User:
class User:
    def __init__(self, name, email_address): # now our method has 2 Parameters!
        self.name = name #and we use the values passed in to set the name attribute
        self.email = email_address # and the same for the email address
        self.account_balance = 0 # the account balance is set to $0, so here no need for a 3rd Parameter

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Pytho", "monty@python.com")
print(guido.name) # Output: Guido van Rossum
print(monty.name) # Output: Monty Pytho