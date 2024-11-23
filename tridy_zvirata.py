class Animal:
    total_weight = 0
    all_animals = []

    def __init__(self, weight, age):
        self.weight = weight
        self.age = age
        Animal.total_weight += weight
        Animal.all_animals.append(self)

    @classmethod
    def get_total_weight(cls):
        return cls.total_weight

    def set_weight(self):
        Animal.total_weight -= self.weight
        self.weight = int(input("set new weight for animal: "))
        Animal.total_weight += self.weight


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


animal1 = Animal(30, 1)
animal2 = Animal(40, 2)
animal3 = Animal(50, 3)


animals = [animal1, animal2, animal3]
for animal in animals:
    print(animal.weight)

print(Animal.get_total_weight())

Animal.set_weight(animal1)
print(animal1.weight)

