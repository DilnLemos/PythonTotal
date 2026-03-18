"""
Práctica sobre Argumentos Indefinidos (*args) 1

Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos

numéricos, y que retorne la suma de sus valores al cuadrado.


Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
"""

def suma_cuadrados(*args):
    total = 0
    for num in args:
        num **= 2
        total += num
    return total
    # return sum([num ** 2 for num in args]) # Otra forma de hacerlo, con comprensión de listas

print(f"Suma de cuadrados: {suma_cuadrados(1, 2, 3)}")

"-----------------------------------------------------------------------------------------------------------------------------"

"""
Práctica sobre Argumentos Indefinidos (*args) 2

Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, 

y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o 

lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
"""

def suma_absolutos(*args):
    total = 0
    for num in args:
        if num < 0:
            total += -num
        else:
            total += num
    return total
    # return sum([abs(num) for num in args]) # Otra forma de hacerlo, con absoluto incorporado en la función sum
    # return sum([num if num >= 0 else -num for num in args]) # Otra forma de hacerlo, con comprensión de listas
    
    "-----------------------------------------------------------------------------------------------------------------------------"
    
"""
Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, 

y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"
"""

def numeros_persona(nombre, *args):
    total = sum(args)
    return f"{nombre}, la suma de tus números es {total}"