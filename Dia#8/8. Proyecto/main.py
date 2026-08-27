from generadores import turnero

def cliente():
    print("Bienvenido señor/a")

    print("""
    Nuestras areas son:
    1. Perfumería
    2. Fármacos
    3. Cosméticos
    0. Salir
    """)

    while True:
        try:
            area = int(input("Elige a que area deseas ir: "))
        except ValueError:
            print("Valor ingresado inválido")
        else:
            if area not in range(0, 4):
                print("Área no disponible")
            else:
                break

    return area



def main():

    while True:

        turno = cliente()
        
        if turno == 0:
            print("Adiós")
            break

        generador = turnero(turno)
        ticket = next(generador)
        print(ticket)
        print("Espere su turno para ser atendido")

if __name__ == "__main__":
    main()