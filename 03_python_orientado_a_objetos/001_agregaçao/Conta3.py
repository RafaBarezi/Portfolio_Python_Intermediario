# Classes e objetos III

class Conta3:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def extrato(self):
        print(f"numero da conta conjunta:{self.numero}\n saldo: {self.saldo}")