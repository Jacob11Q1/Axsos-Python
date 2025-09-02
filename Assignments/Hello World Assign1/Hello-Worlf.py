# Task 1) Print "Hello World"
print("Hello World");

# Task 2) Print "Hello Noelle!" with the name in a variable
name = "Noelle";
print("Hello",name,"!"); # With A Comma
print("Hello " + name + "!"); # With A +

# Task 3) Print "Hello 42!" with the number in a variable
age = 42;
print("Hello" , age ,"!"); # With A Comma
# print("Hello " + age + "!"); # With A +
# The Correct Way is bellow
print("Hello %d" % age + "!");
print("Hello " + str(age)) # Another Option

# Task 4) print "I Love to eat Sushi and Pizza" with the food in variables
fave_food1 = "Sushi";
fave_food2 = "Pizza";
print(f"I Love to eat {fave_food1} and {fave_food2}"); # Method 1) with the F-String
print("I Love to eat {} and {}" .format(fave_food1 , fave_food2)); # Method 2) with the .format Strings