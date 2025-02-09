# Classes e objetos II

class Conta2:
    def __init__(self, cliente, cpf, nome, saldo):
        self.cliente = cliente
        self.cpf = cpf
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerarextrato(self):
        print(f"numero:{self.cliente}\ncpf:{self.cpf}\nsaldo{selfsaldo}") # type: ignore

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ("Transferencia Realizada")