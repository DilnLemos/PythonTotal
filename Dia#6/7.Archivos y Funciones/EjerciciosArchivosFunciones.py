"""
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
"""
def abrir_leer(archivo):
    with open(archivo, "r") as archivo:
        contenido = archivo.read()
    return contenido

def sobrescribir(archivo):
    with open(archivo, "w") as archivo:
        contenido = archivo.write("contenido eliminado")
    return contenido

def registro_error(archivo):
    with open(archivo, "a") as archivo:
        contenido = archivo.write("se ha registrado un error de ejecución")
    archivo.close()
    return contenido
