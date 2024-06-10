""""
13. Implementa la clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos.
El número de cuenta se genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos con el mismo
número de cuenta. La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo, se pondrá a cero inicialmente.
En una cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una cuenta y otra.
No se permite el saldo negativo. En el siguiente capítulo se propone un ejercicio como mejora de éste, en el que se pide
llevar un registro de los movimientos realizados.

Programa principal:

cuenta1 = BankAccount()
cuenta2 = BankAccount(1500)
cuenta3 = BankAccount(6000)
print(cuenta1)
print(cuenta2)
print(cuenta3)
cuenta1.deposit(2000)
cuenta2.withdraw(600)
cuenta3.deposit(75)
cuenta1.withdraw(55)
cuenta2.transfer(cuenta3, 100)
print(cuenta1)
print(cuenta2)
print(cuenta3)
Salida

Número de cta: 6942541557 Saldo: 0,00 €
Número de cta: 9319536518 Saldo: 1500,00 €
Número de cta: 7396941518 Saldo: 6000,00 €
Número de cta: 6942541557 Saldo: 1945,00 €
Número de cta: 9319536518 Saldo: 800,00 €
Número de cta: 7396941518 Saldo: 6175,00 €
"""
import random
from typeguard import typechecked
@typechecked()
class BankAccount():
    __cuentas = set()

    def __init__(self,saldo:float= 0):
        self.__saldo = float(saldo)
        self.__num = self.generarNum()

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if value < 0:
            raise ValueError("ERROR, El saldo no puede ser negativo")

    @staticmethod
    def generarNum():
        numero_cuenta = random.randint(10 ** 9, (10 ** 10) - 1)
        if numero_cuenta not in BankAccount.__cuentas:
            BankAccount.__cuentas.add(numero_cuenta)
        return numero_cuenta

    def depositar(self,saldo):
        if saldo > 0:
            self.__saldo += saldo
            return self.__saldo
        else:
            raise ValueError("ERROR, El saldo tiene que ser positivo")
    def retirar(self,saldo:float):
        if saldo > 0:
            if self.__saldo >= saldo:
                self.__saldo -= saldo
                return self.__saldo
            else:
                return "No hay saldo suficiente"
        else:
            return "La cantidad tiene que ser mayor que 0"
    def transferencia(self,cuenta:__cuentas,saldo:float):
        if saldo > 0:
            if self.__saldo >= saldo:
                self.__saldo -= saldo
                cuenta.__saldo += saldo
                return self.__saldo
        else:
            return "No hay saldo suficiente"


    def __str__(self):
        return f"Número de cuenta: {self.__num} - Saldo: {self.__saldo}€"

def main():
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    cuenta1.depositar(2000)
    cuenta2.retirar(600)
    cuenta3.depositar(75)
    cuenta1.retirar(55)
    cuenta2.transferencia(cuenta3, 100)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
main()