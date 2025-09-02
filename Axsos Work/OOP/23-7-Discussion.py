# # Discussion 23 / 7:
# # OOP: Creating Class Instances and Using Inheritance

# # Avoiding code repetition using inheritance
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def get_info(self):
#         print(f"Human Info -> Name: {self.name}, Age: {self.age}")

# # Developer class inherits from Human
# class Developer(Human):
#     def __init__(self, name, age, position=None):
#         super().__init__(name, age)
#         self.position = position
    
#     def get_info(self):
#         print(f"Developer Info -> Name: {self.name}, Age: {self.age}, Position: {self.position}")
    
#     def get_name(self):
#         print(f"The Name is: {self.name}")

# # Student class inherits from Human
# class Student(Human):
#     def __init__(self, name, age):
#         super().__init__(name, age)
    
#     def get_marks(self):
#         print(f"Student's Info -> Name: {self.name}, Age: {self.age}")

# # BackEnd class inherits from Developer
# class BackEnd(Developer):
#     def __init__(self, name, age, position=None):
#         super().__init__(name, age, position)

# # Instances
# user1 = Human("Jacob", 29)
# omayma = Developer("Omayma", 25, "Front End")
# ahmad = Student("Ahmad", 28)
# mohammad = BackEnd("Mohammad", 24, "Back End")

# # Method calls
# print("=== Human ===")
# user1.get_info()

# print("\n=== Developer ===")
# omayma.get_info()
# omayma.get_name()

# print("\n=== Student ===")
# ahmad.get_marks()

# print("\n=== BackEnd Developer ===")
# mohammad.get_info()  # Inherited from Developer

# Polymarphism Example
class PaymentMethod:
    def pay(self , amount):
        raise NotImplementedError("Subclasses Must implement this Method")

class CriditCardPayment(PaymentMethod):
    def pay(self , amount):
        print(f"Paid ${amount} using Credit Card.")

class PayPalPayment(PaymentMethod):
    def pay(self , amount):
        print(f"Paid ${amount} using PayPal.")

class LahzaPayment(PaymentMethod):
    def pay(self , amount):
        print(f"Paid ${amount} using Bitcoin.")

# Function using polymorphism
def process_payment(payment_method, amount):
    payment_method.pay(amount)

# Instances
credit_card = CriditCardPayment()
paypal = PayPalPayment()
bitcoin = LahzaPayment()

# Driver code
print("=== Processing Payments ===")
process_payment(credit_card, 100)
process_payment(paypal, 50)
process_payment(bitcoin, 250)
