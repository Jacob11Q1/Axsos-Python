# For Loops

# Loops In JavaScript for(var x = 0; x < 10; x++){}

# In Python
for x in range(0 , 10 , 1):
    print(x);
    
for j in range(10 , 0 , -3):
    print(j);
    
# For Loops Through Lists
my_list = ['abc' , 123 , 'xyz'];
for i in range(0 , len(my_list)):
    print(i , my_list[i]);
    
# Or
for v in my_list:
    print(v);
    
# For Loops Through Dictionaries
my_dict = {'Name':'Noelle' , 'Language':'Python'};
for x in my_dict:
    print(x);
    print(x , my_dict[x]);
    
# Option key
capitals = {'Washington':'Olympia' , 'California':'Sacramento' , 'Idaho':'Boise' , 'Illinois':'SpringField'};
    # Onother Way To Iterate through Keys
for key in capitals.keys():
    print(key);

# Onother Way To Iterate through Values
for val in capitals.values():
    print(val);
    
# Onother Way To Iterate through Both Values and Keys
for key , val in capitals.items():
    print(key , ' = ' , val);


# (For Loop)
for count in range(0 , 5):
    print('Looping - ' , count);
    
# The Version Of While Loop Like This
count = 0;
while count < 5:
    print("Looping - " , count);
    count += 1;
    
y = 3;
while y > 0:
    print(y);
    y = y - 1;
else:
    print("Final Else Statement");
    
for val in "String":
    if val == "i":
        break;
    print(val); # Output: S t r

for val in "String":
    if val == "i":
        continue;
    print(val); # Output: S t r n g (No Printing the i String)
    
y = 3;
while y > 0:
    print(y);
    y = y - 1;
    if y == 0:
        break;
else:
    print("Final Else Statement");
    
# Countdown by Fours - # Print positive numbers starting at 2018, 
def countdown(i):
	while i > 0:
		print(i)
		i = i- 1
		if i == 0:
			break;
countdown(2018);