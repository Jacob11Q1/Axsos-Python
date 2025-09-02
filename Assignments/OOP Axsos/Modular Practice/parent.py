# modularizing/parent.py
local_val = "magical unicorns"

# A simple function
def square(x):
    return x * x

# A simple class
class User:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        return "hello"

print("Namespace inside parent.py:", locals())

print("__name__ in parent.py is:", __name__)

if __name__ == "__main__":
    print("The file is being executed directly")
    
    print(square(5))
    user = User("Anna")
    print(user.name)
    print(user.say_hello())
else:
    print("The file is being executed because it is imported by another file. The file is called:", __name__)