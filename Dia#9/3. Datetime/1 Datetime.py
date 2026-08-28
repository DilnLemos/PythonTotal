"""
Libreria que permite guardar fechas y horas, además de hacer operaciones con ellas
"""
import os
import datetime

os.system("clear")

print("--- MANEJO DE HORAS ---")
hora = datetime.time(17, 35, 21) # Crear hora en formato 24hrs HH/MM/SS
print(f"El tipo de dato es: {type(hora)}")
print(f"Mi hora es: {hora}")
print(f"La hora es {hora.hour} con {hora.minute} minutos y {hora.second} segundos.")

print("\n--- MANEJO DE FECHAS ---")

dia = datetime.date(2007, 3, 8) # Crear fecha en formato YY/MM/DD
print(f"Mi dia es {dia.day} del mes {dia.month} del año {dia.year}")
print(f"La fecha es: {dia.ctime()}")

fecha_actual = datetime.date.today()
print(f"La fecha actual es: {fecha_actual}")

print("\n--- CREACIÓN MANUAL COMPLETA ---")

# Utilizamos el método datetime
from datetime import datetime

fecha = datetime(2026, 4, 10, 18, 43, 19, 3000) # Formato de fecha YY/MM/DD - HH/MM/SS/MS
print(f"mi fecha creada es: {fecha}")

fecha = fecha.replace(year = 2023, month = 5) # Modificaciones de fecha
print(f"Nueva fecha {fecha}")

print("\n--- OPERACIONES ENTRE FECHAS Y HORAS---")

#Utilizamos el método date
from datetime import date

nacimiento = date(1988, 11, 27)
defuncion = date(2014, 7, 23)

vida = defuncion - nacimiento
print(f"La persona vivió {vida.days} dias")
print(f"La persona vivió {(vida.days / 365)} años")

despertar = datetime(2026, 4, 11, 7, 30)
duerme = datetime(2026, 4, 11, 23, 45)

vigilia = duerme - despertar
print(f"EStuvo despierto {vigilia.seconds} segundos")