# Printing Strings

print("This is a sample String");

# Option 1)
name = "Matt";
print("My Name is" , name);

# Option 2)
name = "Zen";
print("My name is " + name);

# Strings Interpolation
# F-String

first_name = "Jacob";
last_name = "Qumsiyeh";
age = 29;
print(f"My name is {first_name} {last_name} and I am {age} years old");

# Another Version of Formating
print("My name is {} {} and I'm {} years old." .format(first_name , last_name , age));
print("My name is {} {} and I'm {} years old." .format(age , first_name , last_name));

# Method Formation 1) %s for the string 2) %d for the numbers
hw = "Hello %s" % "World";
py = "I love Python %d" % 3;
print(hw , py);

# Addition to the code above
name = "Zen";
age = 27;
print("My Name is %s and T'm %d years old." % (name,age));

# Built in String Methods
x = "Hello World";
print(x.title());

# The following code below is a strings commonly used
# 1) string.upper(): returns a copy of the string with all the characters in uppercase.
# 2) string.lower(): returns a copy of the string with all the characters in lowercase.
# 3) string.count(substring): retums the number of occurrences of a substring in a string.
# 4) string.split(char): returns a list of values where the string is split at the given character. Without a parameter, the default split is in every space.
# 5) string.find(substring): returns the index of the start of the first occurrence of a substring within the string.
# 6) string.isalnum(): returns a boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include isalpha().isdigit(), islower().isupper(), and so on. All return booleans.
# 7) string.join(list): returns a string concatenated with all strings within our set (in this case, a list).
# 8) string.endswith(substring): returns a boolean based upon whether the last characters of the string match the substring.