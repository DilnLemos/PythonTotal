precios_cafe = [("capuchino", 1.5), ("Expreso", 2.5), ("moká", 1.75)]

for cafe, precio in precios_cafe:
    print(cafe, precio)
    
    
def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ""
    
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
        
    return (cafe_mas_caro, precio_mayor)

print(cafe_mas_caro(lista_precios= precios_cafe))