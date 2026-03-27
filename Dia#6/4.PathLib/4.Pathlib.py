from pathlib import Path

carpeta = Path("C:/Users/Usuario/Desktop/Curso Python/Curso Python/Dia#6")
archivo = carpeta / "texto.txt"

mi_archivo = open(archivo, "r")
print(mi_archivo.read())

"----------------------------------------------------------------------------------------------------"
#Simplificación
ruta = Path("C:/Users/Usuario/Desktop/Curso Python/Curso Python/Dia#6/") / "prueba.txt"
print(ruta) # salida: C:/Users/Usuario/Desktop/Curso Python/Curso Python/Dia#6/prueba.txt

"-----------------------------------------------------------------------------------------------------"
