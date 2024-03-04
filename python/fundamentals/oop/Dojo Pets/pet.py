from ninja import Ninja

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print(f"{self.name} makes a sound!")

class Cat(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "Cat", tricks)

    def noise(self):
        print(f"{self.name} meows!")

pet_instance = Pet("Fluffy", "Cat", ["sit", "fetch"])
ninja_instance = Ninja("John", "Doe", 5, 10, pet_instance)                

# Feed the pet
ninja_instance.feed()

# Walk the pet
ninja_instance.walk()

# Bathe the pet
ninja_instance.bathe()