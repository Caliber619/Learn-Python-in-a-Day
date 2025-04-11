# LIST COMPRESSIONS   (a way of creating lists)


nums = [1,2,3,4,5]

# lets make a new list
numbers_power_2 = [n**2 for n in nums]

print(numbers_power_2)


# older way
numbers_power_2 = []
for n in nums:
    numbers_power_2.append(n**2)

print(numbers_power_2)