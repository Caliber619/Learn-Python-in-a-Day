# decorators
# Decorators in Python are a way to modify or enhance the behavior of functions or methods without changing their actual code. 


# def decorator_function(original_function):
#     def wrapper_function():
#         print("Before the function runs.")
#         original_function()
#         print("After the function runs.")
#     return wrapper_function

# @decorator_function
# def say_hello():
#     print("Hello!")

# say_hello()



def logtime(func):
    def wrapper():
        # do something before
        print("before")
        val = func()
        # do something after
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("Hello")

hello()