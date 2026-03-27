from os import system
system("clear") # Limpia la consola, en Windows se usa "cls"
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))


print(f"Hola {nombre}, tienes {edad} años.")