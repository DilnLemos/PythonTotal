import os
from collections import Counter, defaultdict, namedtuple


# ------ COUNTER ------

"""
Permite contar de forma más efectiva la cantidad de datos que hay en un arreglo, diccionario, etc.
"""

os.system("clear")
print("------ COUNTER ------")
numeros = [2, 3, 4, 6, 1, 23, 5, 3, 1, 5, 6, 9, 7, 6, 5, 3]
print(Counter(numeros))

string = "misissipia"
print(Counter(string))

frase = "Al pan, pan, al vino, vino"
print(Counter(frase.split()))

serie = Counter([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4])
print(serie.most_common())
print(serie.most_common(1))

# ------ DEFAULTDICT ------

"""
Permite modificar el comportamiento de un diccionario cuando se consulte por un valor de una
llave inexistente, modificando el diccionario y creando este nuevo valor a la llave buscada
"""
print("\n------ DEFAULTDICT ------")

dict = {"uno": "verde",
        "dos": "azul",
        "tres": "rojo"}

dict = defaultdict(lambda: "nada", dict) # Se le asigna el valor "nada" a las llaves inexistentes

print(dict) # Diccionario original, pero ya modificado
print(dict["dos"]) # Consulta válida
print(dict["cinco"]) # Consulta inválida, retorna "nada"
print(dict) # Diccionario modificado

# ------ NAMEDTUPLE ------

"""
Permite acceder a valores dentro de lass tuplas por nombres en vez de indices.
"""

print("\n------ NAMEDTUPLE  ------")

Persona = namedtuple("Persona", ["nombre", "edad", "sexo", "peso"]) # Etiqueta para llamar | Estructura de datos

Dilan = Persona("Dilan", 19, "M", 67) # Persona creada a partir de la estructura
print(Dilan.nombre) #  Accesos a través de eitqueta
print(Dilan[1]) # Acceso a través de índice
print(Dilan.sexo) #  Accesos a través de eitqueta
print(Dilan[3]) # Acceso a través de índice
