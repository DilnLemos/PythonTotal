
LETRAS = "abcdefghijklmnopqrstuvwxyz"
PYTHON = "python"
def analizador_texto():
    
# --------------------------------------------------------------------------------------
    texto = input("Ingrese un texto: ")
    letras_buscadas = {}
    for letra in range(1, 4):
        
        while True:
            buscar_letra = input(f"Ingrese la letra {letra} a buscar: ")
            if buscar_letra not in LETRAS:
                print("Letra no válida. Por favor, ingrese una letra del alfabeto.")
            else:
                letras_buscadas[buscar_letra] = texto.lower().count(buscar_letra)
                break
            
# --------------------------------------------------------------------------------------  
    palabras = texto.split()
    
    num_palabras = len(palabras)
    num_caracteres = len(texto)
    print(f"El texto tiene {num_palabras} palabras y {num_caracteres} caracteres.")
    
# --------------------------------------------------------------------------------------
    if PYTHON in texto.lower():
        print("La palabra python se encuentra en el texto")
    else: 
        print("La palabra python no se encuentra en el texto")

# --------------------------------------------------------------------------------------
    print(f"las letras buscadas son:\n {letras_buscadas}")
    
    
def main():
    print(" --- ANALIZADOR DE TEXTO --- ")
    analizador_texto()
    
if __name__ == '__main__':
    main()