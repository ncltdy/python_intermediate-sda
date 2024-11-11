def kalkulacka():
    try:
        a = int(input("zadejte prvni cislo: "))
    except ValueError:
        print("spatne zadana hodnota, ukoncuji program")
        quit()

    operace = input("zadejte znamenko: ")

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
    else:
        print("spatne zadany operator, ukonuji program")
        quit()

print(kalkulacka())
