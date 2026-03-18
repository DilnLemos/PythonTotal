"""
Lista inicial: Palitos
Función Mezcla palitos
Función elección palitos
Función comprobar intento
"""

from random import shuffle

palitos = ["-", "--", "---", "----"]

def mezclar(palitos: list):
    shuffle(palitos)
    return palitos

mezclar(palitos)

def probar_suerte():
    intento = ""
    
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un número del 1 al 4: ")
        
    return int(intento)

def chequeo_intento(palitos, intento):
    if palitos[intento - 1] == "-":
        print("A lavar platos crackd")
    else:
        print("se salvó rey")
    
    print(f"Tu palito fue {palitos[intento - 1]}")
    
palitos_mezclados = mezclar(palitos)
selección = probar_suerte()
chequeo_intento(palitos_mezclados, selección)
