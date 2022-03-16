names = ["john", "jack", "jane"]
for name in names:
    print(name)

print(names[1])

numbers = []
numbers.append(5)
print(numbers)
numbers.append(2)
print(numbers)
numbers.append(-8)
print(numbers)


names = ["john doe", "jack", "jane smith"]
length_of_names = []
for name in names:
    length_of_names.append(len(name))
print(length_of_names)

names = ["john doe", "jack", "jane smith"]
length_of_names = []
for name in names:
    length_of_names.append(name.upper())
print(length_of_names)