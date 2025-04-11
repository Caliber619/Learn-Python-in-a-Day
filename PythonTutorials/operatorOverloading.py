# operator overloading

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # greater than function which compares objects
    def __gt__(self, other):
        return True if self.age> other.age else False


roger = Dog('Roger', 8)
syd = Dog('Syd', 7)
bru = Dog('Bru', 10)


print(roger>syd)
print(roger>bru)




# __add__() respond to the + operator
# __sub__() respond to the - operator
# __mul__() respond to the * operator
# __truediv__() respond to the / operator
# __floordiv__() respond to the // operator
# __mod__() respond to the % operator
# __pow__() respond to the ** operator
# __rshift__() respond to the >> operator
# __lshift__() respond to the << operator
# __and__() respond to the & operator
# __or__() respond to the | operator
# __xor__() respond to the ^ operator