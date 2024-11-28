def generuj_mocniny(cislo):
    for i in range(cislo):
        yield (i+1) ** 2    # yield ma stejnou funkci jako return


for mocnina in generuj_mocniny(5):
    print(mocnina)


def generator_jmen(pred, konec):
    for p in pred:
        yield p + konec


predpona = ["Nico", "Bel", "Daniel"]
koncovka = "le"

for jmeno in generator_jmen(predpona, koncovka):
    print(f"Tvé jméno je {jmeno}")