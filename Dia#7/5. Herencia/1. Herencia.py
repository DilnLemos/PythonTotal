class Animal:
    
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
            
    def nacer(self):
        print("El animal ha nacido")

class Pajaro(Animal):
    pass

print("-" * 30)
print(Pajaro.__bases__)
print(Animal.__subclasses__())
print("-" * 30)

piolin = Pajaro(1, "rojo")
piolin.nacer()
print(piolin.color)
print(piolin.edad)