from pathlib import Path

## Rutas Absolutas
base = Path.home()  # Ruta al directorio home del usuario
print(base)

## Creación de un objeto Path mediante string, siendo una ruta relativa
#Path acepta strings o mismos objetos Path
guia = Path("ruta1", "ruta2", "archivo.txt")
print(guia)

## Concatenar rutas
base = Path.home()  # Ruta al directorio home del usuario

guia = Path(base, "ruta1", "ruta2", "archivo.txt")
print(guia) # salida: /home/dilnlemos/ruta1/ruta2/archivo.txt

## Construcción Rutas a partir de otros objetos Path
base = Path.home()  # Ruta al directorio home del usuario

guia = Path(base, "ruta1", "ruta2", "archivo.txt")
guia2 = guia.with_name("archivo2.txt")  # Cambia el nombre del archivo
print(guia2)

## Obtener el directorio padre
padre = guia.parent #Método parent devuelve el directorio padre de la ruta, puede usarse varias veces para subir varios niveles
print(padre)

## Obtener todos los archivos específicos en un directorio

ruta_act = Path.cwd() / "Dia#6"  # Ruta al directorio actual
print(ruta_act)
archivos = list(Path(ruta_act).glob("*.txt"))  # Devuelve una lista de todos los archivos y directorios en el directorio actual
print(archivos)

### O por medio de un loop
for txt in Path(ruta_act).glob("*.txt"):
    print(txt.name)

## Relatividad de rutas
base = Path("home", "usuario", "documentos", "proyecto")
print(f"base: {base}")
### Contenido desde usuario
usuario = base.relative_to(Path("home", "usuario")) # Devuelve una nueva ruta.
print(f"usuario: {usuario}")