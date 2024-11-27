def velkym(a):
    return a.upper()

jmena = ["Hroch", "Halon", "Velryba", "Moucha"]

print(list(map(velkym, jmena)))
print(list(map(lambda a: a.upper(), jmena  )))

def obsahuje_a(text):
    return "a" in text

print(list(filter(obsahuje_a, jmena  )))
print(list(filter(lambda text: "a" in text, jmena)))

lidi = [("Zdena", 30), ("Albert", 24), ("Martin", 33)]
print(sorted(lidi, key=lambda a: a[0]))

class Lide:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __repr__(self):
        return f"{self.jmeno} {self.vek}"


alb = Lide("Albert", 24)
zd = Lide("Zdena", 30)
ma = Lide("Martin", 33)

navstevnici = [zd, ma, alb]
print(sorted(navstevnici, key=lambda x: x.jmeno))
print(sorted(navstevnici, key=lambda x: x.vek))
