# 10 Challenges on 24 / 7 / 2025 Modified:

# Challenge 1: Even Numbers Printer
def print_even_numbers():
    for num in range(2,11):
        if num % 2 == 0:
            print(f"Even Numbers: {num}")
print_even_numbers()

# Challenge 1: Even Numbers Printer Cleaner Version
def print_even_numbers():
    for num in range(2, 11, 2):  # Start at 2, go up to 10, step by 2
        print(f"Even Number: {num}")
print_even_numbers()

# Challenge 1: Even Numbers Printer Cleaner Version 
# Now Sending it in a list:
def print_even_numbers(numbers):
    even_nums = [] # Creating an empty list to hold even numbers
    for num in numbers:
        if num % 2 == 0:
            even_nums.append(num) # Add even numbers to the list
    return even_nums
my_list = [1,2,3,4,5,6,7,8,9,10]
result = print_even_numbers(my_list)
print(result)

# Challenge 1: The Same but one line code:
def print_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
my_list = [1,2,3,4,5,6,7,8,9,10]
result = print_even_numbers(my_list)
print(result)

# Challenge 2: Count and Print Letters in a word:
def count_letter():
    word = "Python"
    for index in range(len(word)):
        print(f"Letter {index + 1}: {word[index]}")
count_letter()

# Challenge 2: Count and Print Letters in a word: But using enumerate(word)
def count_letter(word):
    for index , letter in enumerate(word):
        print(f"Letter {index + 1}: {letter}")
count_letter("Python") # Example 1
count_letter("AceBro") # Example 2

# Challenge 3: Print Numbers Greater Than 10 From a List:
def greater_than():
    numbers = [4,12,7,15,3,22,8]
    for i in range(len(numbers)):
        if numbers[i] > 10:
            print(numbers[i])
greater_than()

# Challenge 3: The Same Version But No Indexes:
def greater_than():
    numbers = [4,12,7,15,3,22,8]
    for num in numbers:
        if num > 10:
            print(num)
greater_than()
