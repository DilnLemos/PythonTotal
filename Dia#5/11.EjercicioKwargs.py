print("-" * 40)
"""
Crea una función llamada cantidad_atributos que cuente la cantidad de

parémetros que se entregan, y devuelva esa cantidad como resultado.
"""

def cantidad_atributos(**kwargs):
    return len(list(kwargs.items()))

print(cantidad_atributos(x=1, y=2, z=3))

print("-" * 40)

"""
Crea una función llamada lista_atributos que devuelva en forma de lista

los valores de los atributos entregados en forma de palabras clave (keywords).

La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
"""
def lista_atributos(**kwargs):
    return list(kwargs.values())

print(lista_atributos(color_ojos="azules", color_pelo="rubio"))

print("-" * 40)

"""
Crea una función llamada describir_persona, que tome como parámetros su nombre y 

luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

    Características de {nombre}:
    {nombre_argumento}: {valor_argumento}
    {nombre_argumento}: {valor_argumento}
    etc...

Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

    Características de María:
    color_ojos: azules
    color_pelo: rubio
"""

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
        
describir_persona("María", color_ojos="azules", color_pelo="rubio")