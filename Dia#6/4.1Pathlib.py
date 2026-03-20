from pathlib import Path, PureWindowsPath

## Métodos con Path

### Creación de rutas
ruta = Path("/home/dilnlemos/Programación/Python/PythonTotal/Dia#6/prueba.txt")
print(ruta.read_text()) # salida: Hola Mundo, sin necesidad del open o close

"-----------------------------------------------------------------------------"
### Extracción del Nombre
ruta = Path("/home/dilnlemos/Programación/Python/PythonTotal/Dia#6/prueba.txt")
print(ruta.name) # salida: prueba.txt

### Extracción de tipo (sufijo)
print(ruta.suffix) # salida: .txt

### Extracción de nombre sin extensión
print(ruta.stem) # salida: prueba

### Extracción del directorio
print(ruta.parent) # salida: /home/dilnlemos/Programación/Python/PythonTotal/Dia#6

### Extracción de partes de la ruta
print(ruta.parts) # salida: ('/', 'home', 'dilnlemos', 'Programación', 'Python', 'PythonTotal', 'Dia#6', 'prueba.txt')

### Extracción de la ruta absoluta
print(ruta.absolute()) # salida: /home/dilnlemos/Programación/Python/PythonTotal/Dia#6/prueba.txt

### Extracción del propietario del archivo
print(ruta.owner()) # salida: dilnlemos

"-----------------------------------------------------------------------------"
## Métodos booleanos

### Validación de existencia
if not ruta.exists():
    print("El archivo no existe")
else:
    print("El archivo existe") # salida: El archivo existe
    
### Validación de Archivo
if ruta.is_file():
    print("Es un archivo") # salida: Es un archivo
else:
    print("No es un archivo")
    
"-----------------------------------------------------------------------------"
## PureWindowPath
ruta = Path("C:/Users/Usuario/Desktop/Curso Python/Curso Python/Dia#6/prueba.txt")
ruta_windows = PureWindowsPath(ruta)
print(ruta_windows) # salida: C:\Users\Usuario\Desktop\Curso Python\Curso Python\Dia#6\prueba.txt