"""Práctica Abrir y Manipular Archivos 1

Abre el archivo texto.txt e imprime su contenido.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código"""

# Abrir el archivo
archivo = open("Dia#6/texto.txt")
# Leer el contenido del archivo
contenido = archivo.read()
# Imprimir el contenido
print(contenido)
# Cerrar el archivo
archivo.close()

print("-" * 40)
"""
Práctica Abrir y Manipular Archivos 2

Imprime la primera línea del archivo texto.txt

No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
"""

archivo = open("Dia#6/texto.txt")
linea_1 = archivo.readline()
print(linea_1)
archivo.close()

print("-" * 40)

"""
Práctica Abrir y Manipular Archivos 3

Abre el archivo texto.txt e imprime únicamente la segunda línea.

"""

archivo = open("Dia#6/texto.txt")
linea_1 = archivo.readline()
linea_2 = archivo.readline()
print(linea_2)
archivo.close()

print(linea_2)
archivo.close()
