# FizzBuzz Challenge:

for number in range(1,21):
    if number % 5 == 0 and number % 3 == 0:
        print(f"{number}: FizzBuzz")
    elif number % 5 == 0:
        print(f"{number}: Buzz")
    elif number % 3 == 0:
        print(f"{number}: Fizz")
    else:
        print(number)

# List Stats Challenge

# Step 1: Get 5 numbers from the user
numbers = []  # don't use 'list' as variable name
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Step 2: Calculate sum
total = sum(numbers)

# Step 3: Calculate average
average = total / len(numbers)

# Step 4: Find minimum and maximum
minimum = min(numbers)
maximum = max(numbers)

# Step 5: Print results
print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")