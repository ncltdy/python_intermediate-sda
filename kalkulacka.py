def kalkulacka():
    try:
        a = int(input("zadejte prvni cislo: "))
    except ValueError:
        print("spatne zadana hodnota, ukoncuji program")
        quit()

    operace = input("zadejte znamenko: ")
    if operace not in ["+", "-", "*", "/"]:
        raise ValueError("spatne zadane znamenko, ukoncuji program")

    try:
        b = int(input("zadejte druhe cislo: "))
    except ValueError:
        print("spatne zadana hodnota, ukoncuji program")
        quit()

    if operace == "+":
        return a + b
    elif operace == "-":
        return a - b
    elif operace == "*":
        return a * b
    elif operace == "/":
        try:
            return a // b
        except ZeroDivisionError:
            print("nelze delit nulou")


print(kalkulacka())

while True:
    pokracovat = input("prejete si pokracovat ve vypoctech? (y/n): ")
    if pokracovat == "y":
        print(kalkulacka())
    elif pokracovat == "n":
        break


# infinite kalkulacka - zadefinovat operace prvne?

