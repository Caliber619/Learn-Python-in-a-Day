# Exceptions

# try:
#     # some lines of code
# except <ERROR1>:
#     # handle <ERROR1>
# except <ERROR2>:
#     # handle <ERROR2>
# else:
#     # no exceptions raised
# finally:
#     # do something in any case


try:
    result = 2/0
except ZeroDivisionError:
    print("can not divide by zero")
finally:
    result = 1

print(result)  #1

# ----------------------------------------
try:
    raise Exception("An error")
except Exception as error:
    print(error)

# ----------------------------------------

class DogNotFoundException(Exception):
    print("inside")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("dog not found")

# -----------------------------------------

filename = '/Users/ASUS/OneDrive/Desktop/DataScience/PythonTutorials/test.txt'
try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
finally:
    file.close()

# ------------------------------------------

# use with (automatically closes the file)
with open(filename, 'r') as file:
    content = file.read()
    print(content)