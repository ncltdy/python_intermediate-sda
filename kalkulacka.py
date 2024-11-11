def kalkulacka():
    a = int(input("zadejte prvni cislo: "))
    operace = input("zadejte znamenko: ")
    b = int(input("zadejte druhe cislo: "))
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
