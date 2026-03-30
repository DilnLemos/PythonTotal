class Vaca:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"{self.nombre} dice muu")
        
class Oveja:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"{self.nombre} dice mee")
        
vaca = Vaca("Aurora")
oveja = Oveja("Nube")

animales = [vaca, oveja]

"-----------------------------"
for animal in animales:
    animal.hablar()
"-----------------------------"
def animal_hablar(animal):
    animal.hablar()
    

animal_hablar(vaca)
animal_hablar(oveja)
"-----------------------------"