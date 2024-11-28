class IteratorMocnin:
    def __init__(self, cislo):
        self.cislo = cislo
        self.iterace = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterace >= self.cislo:
            raise StopIteration
        self.iterace += 1
        return self.iterace ** 2


mocniny = IteratorMocnin(5)
for mocnina in mocniny:
    print(mocnina)
