from random import choice

PALABRAS = ["python", "programacion", "ahorcado", "desarrollo", "juego"]
LETRAS = "abcdefghijklmnopqrstuvwxyz"

def jugador():
    nombre = input("Ingrese su nombre: ")
    return nombre

def palabra_secreta():
    return choice(PALABRAS)

def ahorcado(nombre, palabra):

    intentos = 6
    p_letras = set(palabra)
    p_oculta = ("_" * len(palabra))
    
    while intentos > 0:
        print("\n" + "-" * 20)
        print(f"Juego Actual: {p_oculta}\nVidas: {intentos}")
        intento = input("Ingrese una letra: ").lower()
        
        if intento in LETRAS and intento in p_letras:
            p_oculta = "".join([letra if letra == intento else p_oculta[i] for i, letra in enumerate(palabra)]) 

        else: 
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} vidas.")
            
        if "_" not in p_oculta:
            print(f"¡Felicidades {nombre}! Has adivinado la palabra: {palabra}")
            break
    else:
        print("\n" + "-" * 20)
        print(f"¡Lo siento {nombre}! Has perdido. La palabra era: {palabra}")   
        


def main():
    nombre = jugador()
    palabra = palabra_secreta()
    ahorcado(nombre, palabra)

if __name__ == "__main__":
    main()