# Herança múltipla é quando herdamos de duas classes ao mesmo tempo

import datetime

class Conta_Poupança:
    def __init__(self, taxa_remuneracao):
        self.taxa_remuneracao = taxa_remuneracao
        self.data_abertura = datetime.datetime.today()

    def Remuneracao_Conta(self):
        self.saldo += self.saldo*self.taxa_remuneracao

class Cliente:
    def __init__(self, nome, endereco, saldo):
        self.nome = nome
        self.endereco = endereco
        self.saldo = saldo

class Extrato:
    def __init__(self):
        self.transacoes = []

    def extrato(self, numeroconta):
        print(f"\nExtrato da conta conjunta: {numeroconta} \n")
        for p in self.transacoes:
            print(f"{p[0]} {p[1]} {p[2]} {p[3]}")

import datetime

class Conta:
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

    def gerar_saldo(self):
        print(f"\nO saldo atual da sua conta é de R$ {self.saldo:,.2f}")

import datetime

class Conta_Remunerada_Poupança(Conta, Conta_Poupança):
    def __init__(self, cliente, numero, saldo, taxa_remuneracao):
        # Como vaiu herdar de Conta e Conta_Poupança, precisamos inicializar os dois
        Conta.__init__(self, cliente, numero, saldo)
        Conta_Poupança.__init__(self, taxa_remuneracao)

    def Remuneracao_Conta(self):
        self.saldo += self.saldo * (self.taxa_remuneracao/30)
        self.saldo -= self.taxa_remuneracao

cliente_1 = Cliente("João", "Rua A", 1000)
cliente_2 = Cliente("Ana", "Rua B", 1000)
Conta_Conj_01 = Conta([cliente_1, cliente_2],
                      "Conta 003", cliente_1.saldo + cliente_2.saldo)
Conta_Poupança_1 = Conta_Poupança(0.1)
Conta_Remunerada_1 = Conta_Remunerada_Poupança(cliente_1, "001", 1000, 5)
Conta_Remunerada_1.Remuneracao_Conta()
Conta_Remunerada_1.gerar_saldo()