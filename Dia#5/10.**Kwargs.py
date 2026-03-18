print("-" * 40)

# Validar que es un diccionario.
def testType(**kwargs):
    print(type(kwargs))
    print(kwargs)

testType(a=1, b=2, c=3)

print("-" * 40)

# Función para acceder a los valores del diccionario.
def acceso(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        
acceso(nombre="Juan", edad=30, ciudad="Madrid")

print("-" * 40)

# Función suma
def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    print(f"Suma total: {total}")
    
suma(a=10, b=20, c=30)

print("-" * 40)

#Combinar con argumentos posicionales
def combinación(num1, num2, *args, **kwargs):
    print(f"num1: {num1}, num2: {num2}")
    
    for i, arg in enumerate(args):
        print(f"arg #{i}: {arg}")
        
    for calve, valor in kwargs.items():
        print(f"{calve} = {valor}")    
        
combinación(1, 2, 3, 4, 5, a=10, b=20)