from pathlib import Path

"""
Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

Recuerda importar Path del módulo pathlib, y utilizar el método home() 
"""

ruta_base = Path.home()
print(ruta_base)

"""
Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

Almacena el directorio obtenido en la variable ruta. No olvides importar Path.

"""

"Curso Python"
"Día 6"
"practicas_path.py"

ruta = Path("Curso Python", "Día 6", "practicas_path.py")
print(ruta)

"""
Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario.
"""

home = Path.home()
ruta = Path(home, "Curso Python", "Día 6", "practicas_path.py")
