
def contar_primos(n):
    if n <= 1:
        return 0
    conteo = 0
    for num in range(2, n + 1):
        es_primo = True
        for divisor in range(2, num - 1):
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            conteo += 1
            print(num)
            
    return conteo
        

def main():
    n = int(input("Ingrese un número entero: "))
    cantidad_primos = contar_primos(n)
    print(f"Cantidad de números primos menores o iguales a {n}: {cantidad_primos}")

if __name__ == "__main__":
    main()