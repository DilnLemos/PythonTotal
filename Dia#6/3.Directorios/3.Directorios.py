import os

# Obtener la ruta del directorio actual
ruta = os.getcwd()
print(ruta)

"------------------------------------------------------------------------------"
#salida: /home/xxxxxx/Programación/Python/PythonTotal/Dia#6

# Cambiar el directorio actual a otro directorio
ruta = os.chdir("/home/dilnlemos/Programación/Python/PythonTotal/Dia#6")
archivo = open("texto.txt", "w")
archivo.close()
"------------------------------------------------------------------------------"
#Crear un nuevo directorio
os.mkdir("/home/dilnlemos/Programación/Python/PythonTotal/Dia#6/Nuevo_Directorio")

"------------------------------------------------------------------------------"
#Separar Ruta

ruta = "/home/dilnlemos/Programación/Python/PythonTotal/Dia#6/3.Directorios.py"

dir = os.path.dirname(ruta)
print(dir) # salida: /home/xxxxxx/Programación/Python/PythonTotal/Dia#6

arc = os.path.basename(ruta)
print(arc) # salida: 3.Directorios.py

tuple = os.path.split(ruta)
print(tuple) # salida: ('/home/xxxxxx/Programación/Python/PythonTotal/Dia#6', '3.Directorios.py')

"------------------------------------------------------------------------------"

#Eliminar un directorio
os.rmdir("/home/dilnlemos/Programación/Python/PythonTotal/Dia#6/Nuevo_Directorio")