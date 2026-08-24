"""def cambiar_letra(tipo):

    def mayuscula(text):
        print(text.upper())

    def minuscula(text):
        print(text.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula

operacion = cambiar_letra("may")

operacion("Hola Mundo")

def cambiar_letra(tipo):

    def mayuscula(text):
        print(text.upper())

    def minuscula(text):
        print(text.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula

operacion = cambiar_letra("may")

operacion("Hola Mundo")
"""


def decorador_saludo(funcion):

    def func_mod(param):
        print("hola")
        funcion(param)
        print("adiós")

    return func_mod


def mayuscula(text):
        print(text.upper())

@decorador_saludo
def minuscula(text):
    print(text.lower())


mayuscula_decorada = decorador_saludo(mayuscula)
mayuscula_decorada("Python total")

minuscula("Python Total")