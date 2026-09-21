"""
Crea una función llamada verificar_email para comprobar si una dirección de email
 es correcta, que verifique si el email dado como argumento contiene "@" (entre el
nombre de usuario y el dominio) y finaliza en ".com" (aunque aceptando también casos
 que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok",
pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario
 "La dirección de email es incorrecta" imprimiendo el mensaje.
"""

import re
def verificar_email(email):

    patron_email = r'\w+@\w+[.]com+'

    verificacion = re.search(patron_email, email)

    if verificacion != None:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

"""
Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento
inicia con la palabra "Hola". Si se encuentra el patrón, la función debe finalizar mostrando
el mensaje "Ok", pero si detecta que la frase no contiene "Hola", debe informarle al usuario
"No has saludado" imprimiendo el mensaje en pantalla.
"""

def verificar_saludo(frase):

    patron_saludo = r'^[Hola]'

    verficacion = re.search(patron_saludo, frase)

    if verficacion != None:
        print("Ok")
    else:
        print("No has saludado")


"""

"""

def verificar_cp(cp):

    patron_cp = r'\w{2}\d{4}'

    verficacion = re.search(patron_cp, cp)

    if verficacion != None:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")