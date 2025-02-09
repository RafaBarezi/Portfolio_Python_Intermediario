# Classes e objetos IV

import datetime
from Extrato import Extrato


class Conta4:
    def __init__(self, clientes, numero, saldo, ):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(
            ["Depósito >>> R$", valor, "\nData >>> ", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["Saque >>> R$", valor, "\nData >>> ", datetime.datetime.today()])
            return True

    def transfereValor(self, contadestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["Transferência >>> R$", valor, "\nData >>> ", datetime.datetime.today()])
            return "Transferencia Realizada"

    def gerarsaldo(self):
        print(f"\nO saldo atual da sua conta é de R${self.saldo}")