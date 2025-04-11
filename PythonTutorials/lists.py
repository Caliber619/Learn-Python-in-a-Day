# lists--------------------------
dogs = ["roger", 1,"SYf",True]
print("roger" in dogs)

print(dogs[0])
# so lists are basically arrays in python but they can have multiple  elements of different data types
# and also we can also traverse negatively

# some list operations
print(dogs[0:3])
print(dogs[2:])
print(len(dogs))
print(dogs.append("judah"))
print(dogs)

# adding a new list at the end
dogs.extend(["judahoo",5])
print(dogs)
dogs += ["heyyo",12]
print(dogs)

# removing from list
dogs.remove("judahoo")
print(dogs)

print(dogs.pop())
print(dogs)

# insert at the list at particular index
items = [1,2,3,45]
# items.insert(2,"Test")
print(items)
# to add multiple items at a single time using slice
# items[1:4] = ["test1","test2"]
print(items)

# sorting the list ... sorting pushes lowercase letters to the end
myList = [2,3,1,4,5]
myList.sort()
print(myList)

myList2 = ["Roger","beau","Beau","Quincy"]
myList2.sort()
print(myList2)
# to fix the upper and lower case issue
myList3 = ["Roger","bob","Beau","Quincy"]
myList3.sort(key=str.lower)
print(myList3)


# to copy items
itemscopy = items[:]
print(itemscopy)

# sorting without modifying
myList4 = ["Roger","bob","Beau","Quincy"]
print(sorted(myList4,key=str.lower))
print(myList4)
