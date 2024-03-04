class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"{self.name}: Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10

class Lion(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.unique_attribute = "mane"

    def display_info(self):
        super().display_info()
        print(f"Unique Attribute: {self.unique_attribute}")

class Tiger(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.unique_attribute = "stripes"

    def display_info(self):
        super().display_info()
        print(f"Unique Attribute: {self.unique_attribute}")

class Bear(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.unique_attribute = "hibernation"

    def display_info(self):
        super().display_info()
        print(f"Unique Attribute: {self.unique_attribute}")

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name, 1, 50, 50))

    def add_tiger(self, name):
        self.animals.append(Tiger(name, 2, 60, 60))

    def add_bear(self, name):
        self.animals.append(Bear(name, 3, 70, 70))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

# Test the Zoo class
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_bear("Yogi")
zoo1.print_all_info()