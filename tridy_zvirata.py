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

    def run(self):
        print("the fish runs")


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


class DomesticFish(Mammal, Fish):
    pass
# kdyz trida dedi z dvou trid a sdili stejnou metodu, zavola se ta ktera je specifikovana jako prvni (mammal)


animal1 = Animal(3, 12)
print(animal1.look())

dog1 = DomesticDog(5, 3, "maltese", "white")
print(dog1)
print(dog1.bark())

fish1 = DomesticFish(1, 1)
print(fish1.run())

