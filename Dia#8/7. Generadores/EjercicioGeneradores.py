"""Crea un generador (almacenado en la variable generador)
que sea capaz de devolver una secuencia infinita de números,
iniciando desde el 1, y entregando un número consecutivo superior
cada vez que sea llamada mediante next.

Pista: Utiliza un loop while para realizar este ejercicio."""

def generadora():
    x = 1
    while True:
        yield x
        x += 1

generador = generadora()

"""
Crea un generador (almacenado en la variable generador)
que sea capaz de devolver de manera indefinida múltiplos de 7,
iniciando desde el mismo 7, y que cada vez que sea llamado
devuelva el siguiente múltiplo (7, 14, 21, 28...).
"""

def generadora_multiplos():
    contador = 1
    while True:
        resultado = 7 * contador
        yield resultado
        contador += 1

generador2 = generadora_multiplos()


"""
Crea un generador que reste una a una las vidas de un personaje
de videojuego, y devuelva un mensaje cada vez que sea llamado:

"Te quedan 3 vidas"
"Te quedan 2 vidas"
"Te queda 1 vida"
"Game Over"

Almacena el generador en la variable perder_vida
"""

def restar_vida():
    vidas = 3
    while True:
        if vidas > 1:
            yield f"Te quedan {vidas} vidas"
        elif vidas == 1:
            yield f"Te queda {vidas} vida"
        else: 
            yield f"Game Over"
        vidas -= 1

perder_vida = restar_vida()
