# Docstrings


def increment(n):
    """ Increment a number """
    return n+1

print(help(increment))

class Dog:
    """ A class representing a dog """
    def ___init___(self, name, age):
        """ Initialize a new dog """
        self.name =  name
        self.age = age
    
    def bark(self):
        """ let the dog bark """
        print("woff!...")

print(help(Dog))