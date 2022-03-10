# Első Python script

print(5)  # Példa, kiir egy egesz szamot
print(500_000)
print(5_000_000)
print(5.2)
print("Hello World")
print('Az ugyfel neve "John Doe"')
print('Hello World')
print("Hello 'World")
print("Az ugyfel neve \"John Doe\"")
print("Az ugyfel neve John\Jack")
print(True)
print(False)

print(type(5))

print("""Aprócska kalapocska, 
      benne csacska""")

favourite_pet = "Kutya"
print(favourite_pet)
favourite_pet = "Macska"
print(favourite_pet)

print(type(favourite_pet))

houses = 12
print(houses)
houses = "sok"
print(houses)

# del(houses)
# print(houses)

# type hint
number_of_cars: int = 16

number_of_cars_in_parking = number_of_cars
print(number_of_cars_in_parking)

number_of_cars_in_parking = 20
print(number_of_cars)
print(number_of_cars_in_parking)

print(len("alma"))
length_of_apple = len("alma")
print(length_of_apple)

print(10 + 10)
print(10 / 6)

print(10.6 - 10)

name = "John Doe"
age = 40
# print(name + " " + age + "eves")

print(name, age, "eves")
print(name, age, "eves", sep="")
print(name, age, "eves", sep="******")

# print(name + " " + age + "eves")
print("alma" + "korte")
fruit1 = "alma"
fruit2 = "korte"
print(fruit1 + fruit2)

print(name + " " + str(age) + " eves")

print(f"A {name} emberke {age} eves")

print(f"A 3 + 5 kifejezés értéke: {3 + 5}")