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
        return a // b

print(kalkulacka())
