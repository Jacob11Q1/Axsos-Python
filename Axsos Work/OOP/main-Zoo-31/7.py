# Zoo Assignment Review on 31 / 7 / 2025:

class animal:
    def __init__(self,name,age = 0,health_lvl = 0 ,happiness_lvl = 0):
        self.name = name
        self.age = age
        self.health_lvl = health_lvl
        self.happiness_lvl = happiness_lvl

    def display_info(self):
        print(f"Hello, Below is your Animal info are: ")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health Level: {self.health_lvl}")
        print(f"Happiness Level: {self.happiness_lvl}")

    def feed(self):
        self.happiness_lvl += 10
        self.health_lvl += 10

class Lion(animal):
    def __init__(self, name, age=0, health_lvl=0, happiness_lvl=0):
        super().__init__(name, age, health_lvl, happiness_lvl)

    def feed(self):
        self.happiness_lvl += 5
        self.health_lvl += 4

class Monkey(animal):
    def __init__(self, name, age=0, health_lvl=0, happiness_lvl=0):
        super().__init__(name, age, health_lvl, happiness_lvl)

    def feed(self):
        self.happiness_lvl += 5
        self.health_lvl += 4

class Tiger(animal):
    def __init__(self, name, age=0, health_lvl=0, happiness_lvl=0):
        super().__init__(name, age, health_lvl, happiness_lvl)

    def feed(self):
        self.happiness_lvl += 5
        self.health_lvl += 4

class Zoo:
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self,animal):
        self.animals.append(animal)
    
    def show_info(self):
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("Internationa Zoo")
zoo1.add_animal(Lion("Simba",3))
zoo1.add_animal(Tiger("Sharokhan",5))
zoo1.add_animal(Monkey("Tarazan",4))
zoo1.animals[1].feed()
print(zoo1.name)
zoo1.show_info()