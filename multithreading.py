import threading


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args =(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result

def scitani(num):
    vysledek_scitani = 0
    for i in range(num):
        vysledek_scitani += i
    return vysledek_scitani

def nasobeni(num):
    vysledek_nasobeni = 1
    for i in range(1, num):
        vysledek_nasobeni *= i
    return vysledek_nasobeni


if __name__ == "__main__":
    t1 = ThreadWithReturnValue(target=scitani, args=(1000000,))
    t2 = ThreadWithReturnValue(target=nasobeni, args=(100,))

    t1.start()
    t2.start()

    print(f"vysledek_scitani = {t1.join()}")
    print(f"vysledek_nasobeni = {t2.join()}")
