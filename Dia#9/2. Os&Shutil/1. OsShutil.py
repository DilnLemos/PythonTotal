import os
import shutil

os.system("clear")
print(os.getcwd()) # Ruta actual de trabajo

archivo = open("curso.txt", "w") # crear archivo nuevo
archivo.write("TExto Preuba") # escribir en archivo
archivo.close # cerrar archivo

# shutil.move("curso.txt", "/home/DilnLemos/PythonTotal/Dia#9") # Mover archivo desde código
# shutil.rmtree("ruta") # ELIMINA TODO LO DE LA RUTA SIN PREGUNTAR NI IMPORTAR QUE HAYA

"""
send2trash, otra librería (externa) util para borrar archivos
send2trash.send2trash("archivo")
"""

# ---- WALK ----

"""
Recorre carpetas, subcarpetas y archivos dentro de una ruta como una función generadora
"""

ruta = os.walk("/home/DilnLemos/PythonTotal/Dia#9")

for carpeta, subcarpeta, archivos in ruta:
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print(f"Los archivos son: ")
    for archivo in archivos:
        print(f"\t{archivo}")
    print("\n")