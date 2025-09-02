# Lambdas Function:
# Lambdas: is an anonymous function

# How we define functions:
def square(num):
    x = num ** 2
    return x
print(square(5))

# The Lambdas way:
lambda num: num **2
lambda num1, num2: num1 + num2

# Lambdas: elements in a list
my_list = ['test_string' , 99 , lambda x: x ** 2] # Creating a new list as an element
# Access the value in the list
print(my_list[2]) # will print a lambda object stored in memory
my_list[2](5) # how to invoke the lambda function

# Passed to another function as a callback:
def invoker(callback):
    print(callback(3))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

# Lambda Stored in variable
add10 = lambda x: x + 10 # storing Lambda expression in a variable
add10(2)
add10(89)
print(add10)

# Returned by another function:
def incremntor(num):
    start = num
    return lambda x: num + x

# Lambdas and Other Functions:
my_arr = [1,2,3,4,5] # Creating a list
def square(num): # Define a function that squares values
    return num ** 2
print(list(map(square, my_arr))) # Invoking map function # Output: [1, 4, 9, 16, 25]

# Ontother Example of the code above:
my_arr = [1,2,3,4,5]
print(list(map(lambda x: x ** 2, my_arr))) # Output: [1, 4, 9, 16, 25]

# Examples To Consider:

# 1) map()
# 2) reduce()
# 3) sort() - lambda is optional on this one
# 4) filter()