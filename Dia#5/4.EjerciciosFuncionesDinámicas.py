"---------------------------------------------------------------------------"

"""
Crea una función donde determine si en una lista los numeros son todos positivos, si encuentra uno nregativo
retorna False, de lo contrario retorna True
"""
def todos_positivos(lista: list):
    for num in lista:
        if num < 0:
            return False
    return True
        
lista_numeros = [-21, 1,2,3,4,5,6, 1001]



"---------------------------------------------------------------------------"
"""
Crea una función que sume los números de una lista que sean mayores a 0 y menores a 1000, y que retorne la suma total
"""


def suma_menores(lista_numeros):
    total = 0
    for num in lista_numeros:
        if num > 0 and num < 1000:
            total += num
        else:
            pass
    return total
print(suma_menores(lista_numeros))

"---------------------------------------------------------------------------"

"""
Crea una función (cantidad_pares) que cuente la cantidad de números pares que
existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
"""
def cantidad_pares(lista_numeros):
    total = 0
    for num in lista_numeros:
        if num % 2 == 0:
            total += 1
        else:
            pass
    return total
    
lista_numeros = [1, 2]