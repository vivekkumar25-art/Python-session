
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} speed: {self.speed}")

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"{self.brand} speed: {self.speed}")


car1 = Car("Toyota")

car1.accelerate(30)
car1.accelerate(20)
car1.brake(10)
car1.brake(50)
