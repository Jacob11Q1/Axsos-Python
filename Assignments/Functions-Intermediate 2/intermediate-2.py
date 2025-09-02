# A- Ubdate values in dictionaries and lists
x = [[5,2,3],[10,8,9]]
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' :'John' , 'last_name' : 'rosales'}
]
sprts_directory = {
    'basketball':['Kobe','Jordan','James','Curry'],
    'football' :['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x':10,'y':20}]

# A-1 Change the value 10 in x to 15
x[1][0] = 15
print(x)

# A-2 change the last name of the first student from Jordan to Bryant
students[0]['last_name'] = "Bryant"
print(students)

# A-3 Change messi to andres
sprts_directory['football'][0] = 'Andres'
print(sprts_directory)

# A-4 Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# B- Iteration Through List
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' :'John' , 'last_name' : 'rosales'},
    {'first_name' :'Mark' , 'last_name' : 'Guillen'},
    {'first_name' :'KB' , 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name,x):
    for name in x:
        print(name[key_name])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

# C- Get values from a list of dictionaries
dojo = {
    'locations': ['San Jose','Seattle','Dalas','Chicago','Tulsa','DC','Burbank'],
    'instructors':['Michael','Amy','Eduardo','Josh','Graham','Patrick','Minh','Devon']
}

def printInfo(x):
    for key,val in dojo.items():
        print(key, " = " , val)
print(printInfo(dojo))