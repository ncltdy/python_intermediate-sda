from dataclasses import dataclass

class Zapas:
    def __init__(self, domaci, hoste, doba):
        self.domaci = domaci
        self.hoste = hoste
        self.doba = doba

    def __repr__(self):
        return f"domaci: {self.domaci}, hoste: {self.hoste}, doba: {self.doba}"

# tyto dve tridy jsou ekvivalentni, dataclass samozpracuje init


@dataclass
class DCZapas:
    domaci: str
    hoste: str
    doba: int

    def print_doba(self):
        print(self.doba)


uefa = DCZapas("Sparta", "Slavia", 93)
cl = Zapas("Liverpool", "Arsenal", 91)

uefa.print_doba()
print(cl.__repr__())