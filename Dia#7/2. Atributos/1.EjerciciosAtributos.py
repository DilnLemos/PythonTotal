"""
Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.
Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.
"""

class Casa:
    
    def __init__(self, color, cantidad_pisos):
        self.color = color  
        self.cantidad_pisos = cantidad_pisos
        
casa_blanca = Casa("blanco", 4)

"""
Crea una clase llamada Cubo, y asígnale el atributo de clase:
    caras = 6
    
y el atributo de instancia:
    color

Crea una instancia cubo_rojo, de dicho color.
"""

class Cubo:
    
    caras = 6
    def __init__(self, color):
        self.color = color
        
cubo_rojo = Cubo("rojo")

"""
Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:
    real = False

Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
    especie = "Humano"
    magico = True
    edad = 17
"""

class Personaje:
    
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
        
harry_potter = Personaje("Humano", True, 17)