# 25 / 7 / 2025 Challenges:

# Challenge 1:
def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers(numbers)

# Challenge 1: store them in a list:
def even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
numbers = [1,2,3,4,5,6,7,8,9,10]
result = even_numbers(numbers)
print(result)

# Challenge 2:
def print_letters():
    word = "Python"
    for i in range(len(word)):
        print(f"Letter {i + 1}: {word[i]}")
print_letters()

# Challenge 3:
def greater_than(numbers):
    grtn10 = []
    for num in numbers:
        if num > 10:
            grtn10.append(num)
    return grtn10
numbers = [4,12,7,15,3,22,8]
result = greater_than(numbers)
print(result)

# Challenge 4:
def split_word():
    word = "Learning Python is fun"
    splt = word.split()
    for i in splt:
        print(i[::-1])
split_word()

# Challenge 5:
def square_even_numbers():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            numbers[i] = numbers[i] ** 2
    print(numbers)
square_even_numbers()

# Challenge 6:
def greet(name):
    print(f"Hello, {name} Welcome!")
greet("Jacob")

# Challenge 7:
def calcualte_area(length , width):
    rec_area = length * width
    return rec_area
result = calcualte_area(8 , 4)
print(result)

# Challenge 8:
def sum_positive(numbers):
    sum = 0
    for i in numbers:
        if i > 0:
            sum += i
    return sum
list = [1,0,-9,7,-6,5,4]
result = sum_positive(list)
print(result)

# Challenge 9:
def count_negative(numbers):
    total = 0
    for i in numbers:
        if i < 0:
            total += 1
    return total
numbers = [3,-1,7,0,-5,10]
result = count_negative(numbers)
print(result)

# Challenge 10:
def find_Largest(numbers):
    large = numbers[0]
    for i in numbers:
        if i > large:
            large = i
    return large
numbers = [50,12,45,78,30,11,25,41]
result = find_Largest(numbers)
print(result)

# Challenge 11:
def find_duplicates(numbers):
    find_dup = []
    for i in numbers:
        if numbers.count(i) > 1 and i not in find_dup:
            find_dup.append(i)
    return find_dup
numbers = [1,2,3,2,4,5,1,6,3,4]
result = find_duplicates(numbers)
print(result)