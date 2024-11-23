def vyprintuj_a_pust(func):
    def nova_funkce(a,b):
        print(f"spoustim funkci \"{func.__name__}\" s parametry {a}, {b}")
        return func(a,b)
    return nova_funkce

@vyprintuj_a_pust
def soucet(a,b):
    return a+b

@vyprintuj_a_pust
def rozdil(a,b):
    return a-b


print(soucet(3,5))
print(rozdil(3,5))