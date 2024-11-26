class Obec:
    pocet_obci = 0

    def __init__(self, pocet_obyvatel):
        self.pocet_obyvatel = pocet_obyvatel
        Obec.pocet_obci += 1

    @classmethod
    def pridej_obec(cls):
        cls.pocet_obci += 2


praha = Obec(1000000)  #praha.pocet_obyvatel - v nějakym místě uchováno
brno = Obec(500000)  #brno.pocet_obyvatel - v jinym místě uchováno
ostrava = Obec(310000)
praha.pocet_obyvatel = 1100000
ostrava.pridej_obec()
Obec.pridej_obec()
print(f"Počet obcí: {praha.pocet_obci}")
print(f"Počet obcí: {brno.pocet_obci}")
print(f"Počet obcí: {Obec.pocet_obci}")
