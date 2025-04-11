# map, filter and reduce
# map: Transforms each item in an iterable using a function.
# filter: Filters items based on a condition (function returns True/False).
# reduce: Applies a function cumulatively to reduce the iterable to a single value.

numbers = [1,2,3,4]

# def double(a):
#     return a*2


# result = map(double, numbers)
# print(list(result))
# result = list(map(double, numbers))
# print(result)


# double = lambda a:a*2
result = list(map(lambda a:a*2, numbers))
print(result)

# ----------------------------------------------------------

def isEven(n):
    return n % 2 == 0

result = filter(isEven,numbers)
# result = filter(lambda n: n%2==0, numbers)
print(list(result))



# ----------------------------------------------------------


# expenses = [('Dinner',70),('car', 129)]    #here is a list of tuples(tuples are immutable)

# sum = 0
# for expense in expenses:
#     sum += expense[1]
# -- this was a long way of doing this

# with reduce we can shorten in
from functools import reduce
expenses = [('Dinner',70),('car', 129),] 
sum = reduce(lambda a,b: a[1]+b[1], expenses)
print(sum)