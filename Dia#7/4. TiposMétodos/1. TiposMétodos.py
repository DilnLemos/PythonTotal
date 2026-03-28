import os
os.system("clear")
class Perro:
    
    vivo = True
    Dueño = False
    
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    
    # Método de instancia, afectan a cada instancia creada
    def ladrar(self):
        print(f"El perro {self.nombre} ladró.")
        
    def cambiar_raza(self):
        self.raza = "Golden"
        print(f"Ahora el perro cambió a la raza {self.raza}, XD")
        self.ladrar() #llamamos a el método ladrar dentro de esta clase

    @classmethod
    def tener_crias(cls, cantidad):
        print(f"Tuvo {cantidad} crias")
        cls.Dueño = False
    
    @staticmethod
    def mirar():
        print(f"El perro está mirando")


raion = Perro("Raion", 5, "Husky")
raion.ladrar()
raion.cambiar_raza()
raion.Dueño = True
print(raion.Dueño)

print("------")
# Acá no necesitamos un objeto o instancia para ejecutar,
# desde la propia clase Perro se puede, pero las instancias también la pueden usar
Perro.tener_crias(6)
raion.tener_crias(5)
print(Perro.Dueño)

print("------")
Perro.mirar()
raion.mirar()