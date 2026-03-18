def suma(A,B):
    return A + B

print(f"Suma estática: {suma(10, 6)}") # Así no da error, recibe el número de argumentos que espera la función

def suma_args(*args):
    return sum(args)

print(f"Suma con args indefinidos: {suma_args(10, 6, 2, 5, 6)}") # Así no da error, recibe el número de argumentos que espera la función (indefinidos)
print(f"Suma con args indefinidos: {suma_args(10, 6)}")
print(f"Suma con args indefinidos: {suma_args(10, 4321, 2)}")

# No se necesita especificamente args, puede ser cualquier nombre, lo importante
# es el asterisco que indica que se pueden recibir argumentos indefinidos
def suma_args(*coso):
    return sum(coso)

print(f"Suma con args indefinidos: {suma_args(10, 6, 2, 5, 6)}") 
print(f"Suma con args indefinidos: {suma_args(10, 6)}")
print(f"Suma con args indefinidos: {suma_args(10, 4321, 2)}")
