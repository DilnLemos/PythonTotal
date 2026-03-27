# Input / Output

# Abrir un archivo
mi_archivo = open("Dia#6/prueba.txt")

# Leemos y mostramos el contenido del archivo
print(mi_archivo.read())

# Cerramos el archivo
mi_archivo.close()  

print("-" * 20)

# Lectura de una linea 
mi_archivo = open("Dia#6/prueba.txt")
print(f"linea 1: {mi_archivo.readline().rstrip()}") #puede ser guardada en una variable y las lineas tienen un salto de line al final, por lo que al imprimir la variable se muestra el salto de linea
# rstrip() elimina los espacios en blanco al final de la linea, incluyendo el salto de linea
print(f"linea 2: {mi_archivo.readline().rstrip()}") # si se vuelve a llamar a readline() se lee la siguiente linea del archivo. readline tiene un guardado para saber cual es la siguiente linea a leer
print(f"linea 3: {mi_archivo.readline().rstrip()}") # si se vuelve a llamar a readline()pero ya no hay mas lineas que leer, se devuelve una cadena vacia

# TODOS ESTOS METODOS DE LECTURA DE ARCHIVOS DEVUELVEN UNA CADENA, POR LO QUE SE LES PUEDEN APLICAR MÉTODOS DE CADENAS

mi_archivo.close()

print("-" * 20)

# Lectura de todas las lineas del archivo
mi_archivo = open("Dia#6/prueba.txt")
for linea in mi_archivo:
    print(linea.rstrip()) # al iterar sobre el archivo, se obtiene cada linea del archivo como una cadena
    
# Otra forma
mi_archivo.seek(0) # seek() mueve el cursor a la posición indicada, en este caso 0 para volver al inicio del archivo
lineas = mi_archivo.readlines() # readlines() devuelve una lista con todas las line
print(lineas) # cada elemento de la lista es una linea del archivo, incluyendo el salto de linea al final de cada linea

# TENER CUIDADO CADA QUE SE EJECUTA ESTE CÓDIGO, SE ABRE EL ARCHIVO PERO NO SE CIERRA, 
# POR LO QUE SI SE EJECUTA VARIAS VECES SE PUEDEN ABRIR VARIOS ARCHIVOS Y AGOTAR LOS RECURSOS DEL SISTEMA, POR ESO ES IMPORTANTE CERRAR EL ARCHIVO CUANDO YA NO SE NECESITA
mi_archivo.close()
