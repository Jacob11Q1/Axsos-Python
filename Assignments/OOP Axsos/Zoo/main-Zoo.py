# Creating A Virtual Zoo Assignment:

# Base Animal Class:
class Animal:
    def __init__(self,name):
        self.name = name
        self.health_level = 100
        self.happiness_level = 100
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Health Level: {self.health_level}")
        print(f"Happiness Level: {self.happiness_level}")
    
    def feed(self):
        self.health_level +=10
        self.happiness_level += 10
        print(f"{self.name} the lion has been fed.")

# Lion Class:
class Lion(Animal):
    def __init__(self, name , size = "Large"):
        super().__init__(name)
        self.size = size
        self.health_level = 80
        self.happiness_level = 90
    
    def feed(self):
        self.happiness_level += 15
        self.health_level += 5
        print(f"{self.name} has been fed.")
    

# Monkey Class:
class Monkey(Animal):
    def __init__(self, name, favourite_food = "Banana"):
        super().__init__(name)
        self.favourite_food = favourite_food
        self.health_level = 70
        self.happiness_level = 120
    
    def feed(self):
        self.happiness_level += 20
        self.health_level += 8
        print(f"{self.name} the monkey has been fed.")


# Bear Class:
class Bear(Animal):
    def __init__(self, name, hibernating = True):
        super().__init__(name)
        self.hibernating = hibernating
        self.health_level = 90
        self.happiness_level = 80
    
    def feed(self):
        self.health_level += 12
        self.happiness_level += 10
        print(f"{self.name} the bear has been fed.")

# Tiger Class:
class Tiger(Animal):
    def __init__(self, name, stripe_count=100):
        super().__init__(name)
        self.stripe_count = stripe_count
        self.health_level = 85
        self.happiness_level = 85

    def feed(self):
        self.health_level += 10
        self.happiness_level += 12
        print(f"{self.name} the Tiger has been fed.")

# Zoo Class:
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_lion(self ,name):
        lion = Lion(name)
        self.animals.append(lion)
    
    def add_Monkey(self ,name):
        monkey = Monkey(name)
        self.animals.append(monkey)
    
    def add_Bear(self ,name):
        bear = Bear(name)
        self.animals.append(bear)
    
    def add_Tiger(self, name):
        tiger = Tiger(name)
        self.animals.append(tiger)
    
    def display_animals(self):
        print(f"--- {self.name} Animals ---")
        for animal in self.animals:
            animal.display_info()
    
    def feed_all(self):
        for animal in self.animals:
            animal.feed()

# Creating The Zoo Name:
my_zoo = Zoo("Vitual Jumanji Zoo")

# Adding Animals To The Zoo:
my_zoo.add_lion("Nala")
my_zoo.add_lion("Simba")
my_zoo.add_Bear("Moneka")
my_zoo.add_Monkey("Bonita")
my_zoo.add_Tiger("Carla")
my_zoo.add_Tiger("Ragnar")

# Displaying The Info Of The Zoo And The Animals:
my_zoo.display_animals()
my_zoo.feed_all()