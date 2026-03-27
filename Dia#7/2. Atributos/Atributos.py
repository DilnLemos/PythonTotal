class Pajaro:
    
    # Atributos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro("rojo", "Tucán")
color_pajaro = mi_pajaro.color
especie_pajaro = mi_pajaro.especie

print(f"Mi pájaro es un {especie_pajaro} de color {color_pajaro}.")

class Perro:
    
    # Atributos de instancia
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        
mi_perro = Perro("Max", "Labrador")
nombre_perro = mi_perro.nombre
raza_perro = mi_perro.raza
print(f"Mi perro se llama {nombre_perro} y es un {raza_perro}.")

class Coche:
    
    # Atributos de clase
    tipo_vehiculo = "Automóvil"
    
    # Atributos de instancia
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
mi_coche = Coche("Toyota", "Corolla")
marca_coche = mi_coche.marca
modelo_coche = mi_coche.modelo
tipo_vehiculo_coche = Coche.tipo_vehiculo
print(f"Mi coche es un {marca_coche} {modelo_coche} y es un {tipo_vehiculo_coche}.")