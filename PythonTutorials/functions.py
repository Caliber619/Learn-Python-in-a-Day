# functions

def hello(name):
    print("Hello "+ name)

hello("Shinigami")

def hello2(name ="defaultName"):
    print("Hello "+ name)

hello2("Litch")
hello2()


def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)

talk("My name is Benimaru Shinmon")



# accessing a variable outside of our scope
def counter():
    count = 0

    def increment():
        # we can provide parameters but if we want to just use the variable of the outer function we can use nonlocal
        nonlocal count
        count = count+2
        return (count)
    
    return increment


# counter()

increment = counter()  
# print(increment)        #garbage value
print(increment())
print(increment())
print(increment())

