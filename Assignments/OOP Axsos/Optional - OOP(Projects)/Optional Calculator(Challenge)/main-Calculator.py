# Challenge Making A Simple Calculator:

print("Welcome To My Simple Project!! - A Simple Calculator")

# Get user input:
number1 = float(input("Enter A Number....: "))
number2 = float(input("Enter A Second Number....: "))

class Calculator:
    def add(self, a , b):
        result = a + b
        print(f"The Sum of 2 numbers is : {result}")
        return self
    
    def subtract(self , a , b):
        result = a - b
        print(f"The Difference between the 2 numbers is: {result}")
        return self
    
    def multiply(self , a , b):
        result = a * b
        print(f"The Product of the 2 numbers is: {result}")
        return self
    
    def divide(self , a , b):
        if b == 0:
            print("Error, You Cant Divide by Zero")
        else:
            result = a / b
            print(f"The Division result is: {result}")
        return self

# Creating a Calculator Object and Using It:
calc = Calculator()
calc.add(number1 , number2).subtract(number1 , number2).multiply(number1 , number2).divide(number1 , number2)