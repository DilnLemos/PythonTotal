"""
La función incorporada en Python len() tiene un comportamiento polimórfico,
ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros),
devolviendo la cantidad de items o caracteres que lo componen.
Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla
y muestre en pantalla (print()) para cada uno de ellos su longitud con la función len().

Puedes recordar cómo implementar la función len() siguiente enlace: https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html
"""

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for item in palabra, lista, tupla:
    print(len(item))

"""
Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.

Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai,
llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases
anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.
"""

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
mago = Mago()
arquero = Arquero()
samurai = Samurai()

personajes = [arquero, mago, samurai]

for personaje in personajes:
    personaje.atacar()

"""
Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.

Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), 
y ejecutar su método defender() independientemente de qué tipo de personaje se trate.
"""

class Mago2():
    def defender(self):
        print("Escudo mágico")

class Arquero2():
    def defender(self):
        print("Esconderse")

class Samurai2():
    def defender(self):
        print("Bloqueo")


def personaje_defender(personaje):
    personaje.defender()
