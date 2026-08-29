import os
import time
import timeit

"""
Libreria que permite hacer medición de tiempos de ejecución
"""
def prueba_for(numero):
    lista = []

    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

os.system("clear")

print("--- PRUEBA CON TIME ---")

"""
Tenemos medido el tiempo en una única ejecución de las funciones
"""

inicio = time.time()
prueba_for(100000)
fin = time.time()
print(f"Tiempo de ejecución ciclo for: {fin - inicio}")


inicio = time.time()
prueba_while(100000)
fin = time.time()

print(f"Tiempo de ejecución ciclo while: {fin - inicio}")

print("\n PRUEBA CON TIMEIT ---")

"""
Hace varias medidas de una misma función en loop determinado y da un promedio
"""

declaracion_for = """
prueba_for(10)
"""

setup_for = """
def prueba_for(numero):
    lista = []

    for num in range(1, numero + 1):
        lista.append(num)
    return lista
"""



duracion_for = timeit.timeit(declaracion_for, setup_for, number = 100000)
print(f"timepo con timeit for: {duracion_for}")


declaracion_while = """
prueba_while(10)
"""

setup_while = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

duracion_while = timeit.timeit(declaracion_while, setup_while, number = 10000)
print(f"tiempo con timeit while: {duracion_while}")