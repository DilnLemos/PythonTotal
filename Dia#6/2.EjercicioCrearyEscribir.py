
"""
Práctica Crear y Escribir Archivos 1

Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
"""
archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()

archivo = open("mi_archivo.txt", "r")
print(archivo.read())


"-----------------------------------------------------------------------------------------------------------------------"

"""
Práctica Crear y Escribir Archivos 2

Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
"""

liena = "Nuevo inicio de sesión"

archivo = open("mi_archivo.txt", "a")
archivo.write(liena)
archivo.close()

archivo = archivo = open("mi_archivo.txt", "r")
print(archivo.read())

"-----------------------------------------------------------------------------------------------------------------------"

"""
Práctica Crear y Escribir Archivos 3

Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.
"""

registro_ultima_sesion = ["Federico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga\t"]

arc = open("registro.txt", "a")
arc.writelines(registro_ultima_sesion)
arc.close()

arc = open("registro.txt", "r")
print(arc.read())