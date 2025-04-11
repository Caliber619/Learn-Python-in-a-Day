# Tuples (are similar to list but unlike list they are immutable)
names = ("roger","syd","Beau")
names[0]
names.index("roger")

print(names)
print("roger"in names)
names[0:2]
sorted(names)
print(names)
newTuple = names + ("tina",)     #do not forget the comma 
print(newTuple)
