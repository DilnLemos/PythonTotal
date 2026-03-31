import random
from Cliente import Cliente
import os

def crear_cliente():
    os.system("clear")
    print("--- Menú Para Crear Usuario ---")
    nombre = input("Ingrese su nombre: ").capitalize()
    apellido = input("Ingrese su apellido: ").capitalize()
    numero_cuenta = random.randint(1000, 9999)
    cliente = Cliente(nombre, apellido, numero_cuenta)

    return cliente

def inicio():
    mi_cliente = crear_cliente()
    os.system("clear")
    print("--- Bienvenido, sus datos de cuenta son: ---\n")
    print(mi_cliente)
    
    sesion = True
    while sesion:
        print("\n--- Menú ---")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Mostrar datos de la cuenta")
        print("4. salir")
        opcion = int(input("\nIngrese una opción: "))
        
        if opcion == 1:
            print("\n--- Menú para Depositar ---")
            deposito = int(input("Ingrese la cantidad a depositar: "))
            mi_cliente.depositar(deposito)

        elif opcion == 2:
            print("\n--- Menú para Retirar ---")
            retiro = int(input("Ingrese la cantidad a retirar: "))
            mi_cliente.retirar(retiro)

        elif opcion == 3:
            print("Datos de la cuenta:\n")
            print(mi_cliente)

        elif opcion == 4:
            sesion = False
        
        else:
            print("Opción inválida")
    
    print("Gracias por utilizar nuestros servicios")










def main():
    inicio()

if __name__ == '__main__':
    main()