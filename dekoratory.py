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


def with_password(func):
    def pass_protected(*args, **kwargs):
        password = "1234"
        if input("zadejte heslo: ") == password:
            return f"vysledek funkce \"{func.__name__}\" je: {func}"
        else:
            return "spatne heslo"
    return pass_protected

@with_password
def soucetAB(a,b):
    return a + b
