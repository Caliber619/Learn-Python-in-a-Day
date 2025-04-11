#Classes

# every class is a type of object
class Animal:
    def walk(self):
        print("walking...")

class Dog(Animal):
    def bark(self):
        print("woof!")
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# roger = Dog()
# print(type(roger))

roger = Dog("tuffy",5)
print(roger.name)
print(roger.age)
roger.bark()

roger.walk()