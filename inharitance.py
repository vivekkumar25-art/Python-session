class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof! Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow! Meow!")


animals = [
    Dog("Tommy"),
    Cat("Kitty")
]

for animal in animals:
    animal.speak()