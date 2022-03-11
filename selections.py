number = 200
if number < 100:
    print("A szam kisebb, mint szaz")
print("End")

number = 0
if number < 0:
    print("Negatív")
    print("Szám")
elif number == 0:
    print("Nulla")
    print("Szám")
else:
    print("Pozitív")
    print("Szám")

number = 100
if number % 2 == 0:
    print("paros")
else:
    print("paratlan")

numbers = [123, 1231, 123, 14, -12, -123, 10, -210]
result = 0
for number in numbers:
    if number > 0:
        result += number
print(result)