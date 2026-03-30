class Padre:
    
    def hablar(self):
        print("Hola")

class Madre():
    
    def reir(self):
        print("ja ja ja")

    def hablar(self):
        print("Que tal?")


class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

nieto = Nieto()
nieto.hablar()
nieto.reir()

print(Nieto.__mro__)
