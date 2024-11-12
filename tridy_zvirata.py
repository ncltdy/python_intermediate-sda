class Animal:
    def __init__(self, weight, age):
        self.weight = weight
        self.age = age

    def look(self):
        print("the animal looks over yonder")

    def breathe(self):
        print("the animal takes a breath of fresh air")


class Fish(Animal):
    def swim(self):
        print("the fish swims")


class Mammal(Animal):
    def run(self):
        print("the mammal runs")


class Bird(Animal):
    def fly(self):
        print("the bird flies")


class DomesticDog(Animal):
    def __init__(self, weight, age, breed, coat_color):
        super().__init__(weight, age)
        self.breed = breed
        self.coat_color = coat_color

    def bark(self):
        print("the dog barks")

    def retrieve(self):
        print("the dog retrieves the ball")


animal1 = Animal(3, 12)
print(animal1.look())

dog1 = DomesticDog(5, 3, "maltese", "white")
print(dog1)
print(dog1.bark())