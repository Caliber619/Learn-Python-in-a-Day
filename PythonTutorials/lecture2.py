name = "caliber"
age = 20

print(type(name)==str)
print(isinstance(name, str))

# age = float(20)
# or
age = float(age)
print(isinstance(age, float))

# ternary operation
def is_adult(age):
    return True if age>18 else False

# multiline string with """  """
print("""Caliber is
29   
years old
""")
print("caliber".upper())
print("caliber".title())
print("caliber".islower())
# other string built-in methods are 
# ** they return a new modified string, so the original string is not modified **
# startswith() endswith() replace() split() strip() join() find()

# some special functions
print(len(name))
print("ali" in name)

# escape sequence use ->  \ plus "anysign"
print("cali\'ber'")
print("cali\n'ber'")   #new line

# indexing in the string
print(name[0])
print(name[0:3])  #slicing using a colon

# imaginary numbers
num = 2+3j
print(type(num))
num2 = complex(2,3)
print(num2)
print(type(num))
print(num.real, num.imag)

# built-in functions for the numbers
# abs, round, round(num,rounduptoplaces)

# enum se hum apne custom enums bana skte hain
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE)
print(State.ACTIVE.value)


age = input("what is your age")
print("Your age is "+ age)


