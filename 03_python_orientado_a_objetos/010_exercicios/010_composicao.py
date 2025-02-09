from agregacao import Cliente

class Extrato:
    def __init__(self):
        self.transacoes = []
    def imprimir(self):
        for p in self.transacoes:
            print(p[0], p[1])

# fazendo uma composição no relacionamento estrutural: 

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPÓSITO", valor])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor])
            return True

cliente_01 = Cliente("123.456.789-10", "Ana", "Rua A")
cliente_02 = Cliente("101.234.567-89", "Pedro", "Rua B")
cliente_03 = Cliente("891.112.345-67", "João", "Rua C")
cliente_04 = Cliente("678.910.123-45", "Maria", "Rua D")

conta = Conta([cliente_01, cliente_02], "Conta 004", 2500.00)

conta.depositar(1000)
conta.sacar(500)
conta.extrato.imprimir()
print("\n")