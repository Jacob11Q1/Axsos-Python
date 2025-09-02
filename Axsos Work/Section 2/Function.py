# Functions:
# Example 1
def add(a,b): # Function Name: 'add', Parameters: a and b
    x = a + b
    return x
new_val = add(5,7) # Calling the add function, with arguments 5 and 7
print(new_val) # Output: 12

# Example 2
def say_hi(name):
    print(f"Hi, {name}")
say_hi("Jacob")
say_hi("Jordan")
say_hi("Majd")
greeting = say_hi("Micheal")
print(greeting)

def add1(a,b):
    x = a + b
    return x
sum1 = add1(4,6)
sum2 = add1(1,4)
sum3 = sum1 + sum2
print(sum3)