"""
Crea un método estático respirar() para la clase Mascota. 
Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
"""


class Mascota:
    
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()

"""
Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.
"""

class Jugador:
    
    vivo = False
    
    @classmethod
    def revivir(cls):
        cls.vivo = True
        
print(Jugador.vivo)
Jugador.revivir()
print(Jugador.vivo)

"""
Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje,
que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.
"""

class Personaje:

    def __init__(self, cantidad_flechas: int):
        self.cantidad_flechas = cantidad_flechas
        
        
    def lanzar_flecha(self):
        self.cantidad_flechas -= 1