import time
from datetime import datetime


class TimeMeasurement:
    def __enter__(self):
        print(f"spusteno v case {datetime.now()}")
        self.zacatek = time.time()

    def __exit__(self, a, b, c):
        print(f"dokonceno v case {datetime.now()}")
        doba = time.time() - self.zacatek
        print(f"ubehly cas: {doba:.2f} vterin")


with TimeMeasurement() as t:
    cislo = 1
    for i in range(10000000):
        cislo += i
    print(cislo)
