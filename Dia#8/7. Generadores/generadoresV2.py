def lista_cuadrados(n):
    cuadrados = []
    for x in range (1, n + 1):
        cuadrados.append(x ** 2)
    return cuadrados

def lista_cuadrados_generadora(n):
    for x in range(1, n + 1):
        yield x ** 2


cuadrados = lista_cuadrados(5)
generadora = lista_cuadrados_generadora(5)

print(cuadrados)
print(next(generadora))
print("Linea de estorbo")
print(next(generadora))

"""
[1, 4, 9, 16, 25]
1
Linea de estorbo
4
"""