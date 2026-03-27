# Modo Lectura
archivo = open("Dia#6/texto.txt", "r")

#Intento de Escritura
try:
    archivo.write("Hola Mundo") # Esto no funciona porque el archivo se abrió en modo lectura, por lo que no se pueden escribir datos en el archivo
except Exception as e:
    print(f"Error: {e}")
finally:
    archivo.close()

"----------------------------------------------------------------------------------------------------"

# Modo Escritura, si el archivo no existe se crea, si el archivo existe se borra su contenido y se escribe el nuevo contenido
archivo = open("Dia#6/texto.txt", "w") 
archivo.write("Hola Mundo") # Esto funciona porque el archivo se abrió en modo escritura, por lo que se pueden escribir datos en el archivo, creando un nuevo archivo o sobrescribiendo el contenido del archivo si ya existe
archivo.close()

"----------------------------------------------------------------------------------------------------"

# Modo Agregar, si el archivo no existe se crea, si el archivo existe se mantiene su contenido y se agrega el nuevo contenido al final del archivo
archivo = open("Dia#6/prueba.txt", "a")
archivo.write("Hola Mundo\n") # Esto funciona porque el archivo se abrió en modo agregar, por lo que se pueden escribir datos en el archivo, creando un nuevo archivo o agregando contenido al final del archivo si ya existe
#IMPORTANTE AGREGAR UN SALTO DE LINEA AL FINAL DEL TEXTO PARA QUE EL NUEVO CONTENIDO SE AGREGUE EN UNA NUEVA LINEA, SI NO SE AGREGA EL SALTO DE LINEA EL NUEVO CONTENIDO SE AGREGARÁ EN LA MISMA LÍNEA QUE EL CONTENIDO ANTERIOR
archivo.close()

"----------------------------------------------------------------------------------------------------"

#Múltiples escrituras, pasando una lista de strings.
archivo = open("Dia#6/prueba.txt", "a")
archivo.writelines(["1\n", "2\n", "3\n", "4\n", "5\n"]) 

archivo.close()