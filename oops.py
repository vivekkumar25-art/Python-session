
# class Car:
#     def __init__(self, brand, speed=0):
#         self.brand = brand
#         self.speed = speed

#     def accelerate(self, amount):
#         self.speed += amount
#         print(f"{self.brand} speed: {self.speed}")

#     def brake(self, amount):
#         self.speed = max(0, self.speed - amount)
#         print(f"{self.brand} speed: {self.speed}")


# car1 = Car("Toyota")

# car1.accelerate(30)
# car1.accelerate(20)
# car1.brake(10)
# car1.brake(50)





# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def withdrawmoney(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("withdrawn successfully")
#             print("Remaining balance:", self.balance)
#         else:
#             print("You don't have enough money")


# A1 = Account("Sushil", 20000)
# A2 = Account("Dilip", 30000)

# print(A1.name)
# print(A1.balance)

# A1.balance = 2500
# print(A1.balance)

# A1.withdrawmoney(500)



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def intro(self):
#         print(f"my name is {self.name} \nmy age is {self.age}")

# class Student(Person):
#     pass

# s1 = Student("vivek", 21)
# s1.intro()
