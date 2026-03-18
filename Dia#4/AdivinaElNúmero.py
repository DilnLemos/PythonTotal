import random

def jugador():
    nombre = input("Ingresa tu nombre: ")
    print(f"¡Bienvenido, {nombre}! Comencemos el juego.")
    return nombre

def juego(nombre):
    
    numero = random.randint(1, 100)
    dificultades = {1: "fácil", 2: "medio", 3: "difícil"}
    while True:
        try:
            dificultad = int(input("Selecciona la dificultad (1: fácil, 2: medio, 3: difícil):"))
            if dificultad in dificultades:
                if dificultad == 1:
                    intentos = 10
                elif dificultad == 2:
                    intentos = 5
                else:            
                    intentos = 3
                break
            else:
                print("Por favor, selecciona una dificultad válida (1, 2 o 3).")
        except ValueError:
            print("Por favor, ingresa un número válido.")
            
    print(f"Has seleccionado la dificultad {dificultades[dificultad]}.")
    print(f"El número que debes adivinar está entre 1 y 100. Tienes {intentos} intentos.")
    
    for intento in range(1, intentos + 1):
        while True:
            try:
                adivinanza = int(input(f"Intento {intento}: Ingresa tu adivinanza: "))
                if 1 <= adivinanza <= 100:
                    break
                else:
                    print("Por favor, ingresa un número entre 1 y 100.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        
        if adivinanza < numero:
            print("Demasiado bajo. Intenta de nuevo.")
        elif adivinanza > numero:
            print("Demasiado alto. Intenta de nuevo.")
        elif adivinanza == numero:
            print(f"¡Felicidades, {nombre}! Has adivinado el número en {intento} intentos.")
            break
        else:
            print(f"Lo siento, {nombre}. El número era {numero}.")
            
def main():
    nombre = jugador()
    juego(nombre)

if __name__ == "__main__":
    main()

