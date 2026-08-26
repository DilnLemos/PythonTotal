def mi_función():
    return 4

def mi_generador():
    yield 4

print(mi_función())
print(mi_generador())

# Variable que almacena la función
valor_producido = mi_generador()

# Llamada a la próxima generación de la función
print(next(valor_producido))

# Si se intenta producir otra vez dará error, porque solo
# produce un único 4.
print(next(valor_producido))

"""
1. 4
2. <generator object mi_generador at 0x7faec86da680>
3. 4
4. print(next(valor_producido))
          ~~~~^^^^^^^^^^^^^^^^^
    StopIteration
"""