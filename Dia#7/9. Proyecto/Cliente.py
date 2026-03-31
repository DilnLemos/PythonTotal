from Persona import Persona
import os
class Cliente(Persona):
    
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nBalance: ${self.balance}"

    def depositar(self, deposito):
        os.system("clear")
        if deposito > 0:
            self.balance += deposito
            print("Depósito aceptado\n")
        else:
            print("No se puede depositar esa cantidad\n")
        
        

    def retirar(self, retiro):
        os.system("clear")
        if retiro > 0:
            if retiro <= self.balance:
                self.balance -= retiro
                print("Retiro aceptado\n")
            else:
                print("No tiene fondos suficientes\n")
        else:
            print("No se puede retirar esa cantidad\n")
