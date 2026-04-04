try:
    numero = int(input("Ingresa un número: "))
except:
    print("Eso no es un número")
else:
    print("Todo salió bien, el número es:", numero)
finally:
    print("Fin del programa")