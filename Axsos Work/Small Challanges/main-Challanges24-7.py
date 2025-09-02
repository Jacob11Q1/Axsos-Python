# Challanges to practice Python 24 / 7 / 2025:

# Challenge 1:
def print_even_numbers():
    for num in range(1 , 11):
        if num % 2 == 0:
            print(num)
print_even_numbers()

# Challenge 2:
def count_letter():
    word = "Python"
    for i in range(len(word)):
        print(f"Letter {i + 1}: {word[i]}")
count_letter()

# Challenge 3:
def find_big_numbers():
    numbers = [4,12,7,15,3,22,8]
    for num in numbers:
        if num > 10:
            print(num)
find_big_numbers()

# Challenge 4:
def reverse_each_word():
    word = "Learning Python is fun"
    splt = word.split()
    for index in splt:
        print(index[::-1])
reverse_each_word()

# Challenge 5:
# My Version Correct but needs to print it inside the list
# def square_even_numbers():
#     numbers = [1,2,3,4,5,6,7,8,9,10]
#     for num in numbers:
#         if num % 2 == 0:
#             print(num ** 2)
#         else:
#             print(num)
# square_even_numbers()

# Another Version of it:
def square_even_numbers():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            numbers[i] = numbers[i] ** 2
    print(numbers)
square_even_numbers()

# Challenge 6:
def greet(name):
    print(f"Hello, {name}! Welcome!")
greet("Jacob")

# Challenge 7:
def calculate_area(length , width):
    rectangle_area = length * width
    return rectangle_area

area = calculate_area(8 , 4)
print(area)

# Challenge 8:
def sum_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

result = sum_positive_numbers([3,-1,7,0,-5,10])
print(result)

# Challenge 9:
def count_negative_numbers(numbers):
    count = 0
    for num in numbers:
        if num < 0:
            count += 1
    return count
result = count_negative_numbers([3, -1, 7, 0, -5, 10])
print(result)

# Challenge 10:
def find_largest(numbers):
    large = numbers[0]
    for num in numbers:
        if num > large:
            large = num
    return large

result = find_largest([3, -1, 7, 0, -5, 10])
print(result)