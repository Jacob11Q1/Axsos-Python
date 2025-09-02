# Data Types

is_hungry = True; # Boolean
has_freckles = False; # Boolean

# Numbers - Integers
age = 35; # Storing an INT
weight = 160.57; # Storing A Float

name = "Joe Blue" # String (Literal Text)

# Composite Types
# 1) Tuples:
dog = ('Bruce' , 'cooker spaniel' , 19 , False);
print(dog[0]); # Output: Bruce
# dog[1] = 'dachshund' it can not be modified ('Tuples' objects does not support item assignment)

# 2) List:
empty_list = [];
ninjas = ['Rozen' , 'KB' , 'Oliver'];
print(ninjas[2]); # Output: Oliver
ninjas[0] = 'Francis' # Modifiying the 0 Element in ninjas
ninjas.append('Micheal');
print(ninjas); # Output: ['Francis', 'KB', 'Oliver', 'Micheal']
ninjas.pop(); 
print(ninjas); # Output: ['Francis', 'KB', 'Oliver'] # Removing The Last Element in the Array ninjas
ninjas.pop(1); 
print(ninjas); # Output: ['Francis', 'Oliver'] # Removing The [1] Element in the Array ninjas

# 3) Dictionaries:
empty_dict = {};
new_person = {'Name': 'John' , 'Age': 38 ,  'Weight': 160.2 , 'has_Glasses' : False};
new_person['Name'] = 'Jack'; # Update if the key does exist
new_person['Hobbies'] = ['Rugby' , 'Basketball' , 'F1 - Fan']; # Adds a key if it does not exist
print(new_person); # Output: {'Name': 'Jack', 'Age': 38, 'Weight': 160.2, 'has_Glasses': False, 'Hobbies': ['Rugby', 'Basketball', 'F1 - Fan']}
w = new_person.pop('Weight'); # Removes the specified Key and returns the value
print(w);
print(new_person);

# Commong Functions
print(type(2.63)); # Output: <class 'float'>
print(type(new_person)); # Output: <class 'dict'>
print(len(new_person)); # Output: 4 (The Number Of Key Value Pairs)
print(len('Coding Dojo')); # Output: 11

# Type Casting or Explicit Type Conversion
# print("Hello" + 42); Output: Type Error
print("Hello " + str(42)); # Output: Hello 42

# Another Example
total = 35;
user_val = "26";
# total = totatl + user_val; # Output: Type Error
total = total + int(user_val);
print(total); # Output: 61