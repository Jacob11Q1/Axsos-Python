# Project Pet Managmement System:

pet_name = input("Enter Your Pet Name Here: ")
pet_type = input("Enter Your Pet Type Here: ")

class Pet:
    def __init__(self , name , animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hunger_level = 5
        self.energy = 100
    
    def feed(self):
        if self.hunger_level > 0:
            self.hunger_level -= 2
            if self.hunger_level < 0:
                    self.hunger_level = 0
                    print("The hunger has decreased.")
        else:
            print("Your pet is not hungry right now.")
        return self
    
    def play(self):
        if self.energy > 0:
            self.energy -= 10
            if self.energy < 0:
                self.energy = 0
                print("Your pet played and had fun! Energy decreased.")
        else:
            print("Your pet is too tired to play.")
        return self
    
    def status(self):
        print(f"\n📋 {self.name}'s Status:")
        print(f"  - Type        : {self.animal_type}")
        print(f"  - Hunger Level: {self.hunger_level}/10")
        print(f"  - Energy Level: {self.energy}/100\n")
        return self

# Create a pet instance
my_pet = Pet(pet_name, pet_type)

# Interact with the pet
my_pet.status()
my_pet.feed().status()
my_pet.play().status()