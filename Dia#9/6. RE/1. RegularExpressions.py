import re

frase = "Si necesitas ayuda llama al númro (658)-598-9977 los operadores funcionarán siempre para la ayuda"

patron = "ayuda"
busqueda = re.search(patron, frase)
print(busqueda)
print(busqueda.start(), busqueda.end())

# ----

busqueda_total = re.findall(patron, frase)
print(busqueda_total)

# ----
for hallazgo in re.finditer(patron, frase):
    print(hallazgo.span())

# ----

texto_num = "llamar al 555-123-4675 ya"


formato = r"\d{3}-\d{3}-\d{4}" # Formato simplificado
otro_formato = r"\d\d\d-\d\d\d-\d\d\d\d" # Formato completo
agrupacion_formato = re.compile(r"(\d{3})-(\d{3})-(\d{4})") #Formato que permite coger cada grupo individualmente


resultado = re.search(formato, texto_num)
resultado1 = re.search(otro_formato, texto_num)
resultado2 = re.search(agrupacion_formato, texto_num)

print(resultado.group())
print(resultado1.group())
print(resultado2.group(1))

# ----
clave = input("ingrese su contraseña: ")
patron = r'\D{1}\w{7}'

respuesta = re.search(patron, clave)
print(respuesta)