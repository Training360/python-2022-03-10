min = 1
max = 100

# DRY - don't repeat yourself
print(f"Gondolj egy számra {min} és {max} között!")

answer = "x"
prev_guess = -1
guess = -2
while answer != "e":
    prev_guess = guess
    guess = (min + max) // 2
    if guess == prev_guess:
        print("Ne szórakozz!")
        answer = "e"
    else:
        print(f"""A szám amire gondoltam: {guess}
        Válassz kérlek!

        e - egyenlő
        k - kisebb
        n - nagyobb
        """)
        answer = input("Mi a válaszod?")

        if answer == "k" or answer == "K":
            max = guess
        elif answer == "n" or answer == "N":
            min = guess
        elif answer == "e" or answer == "E":
            print(f"Eltaláltam, a szám a {guess}")
        else:
            print("Ez NEM válasz!")

