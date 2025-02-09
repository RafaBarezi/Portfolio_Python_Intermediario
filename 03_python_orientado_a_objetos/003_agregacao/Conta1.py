# Classes e objetos I

class Conta1:
    def __init__(self, cliente, cpf, nome, saldo):
        self.cliente = cliente
        self.cpf = cpf
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def valor_em_conta(self):
        print(
            f"\nCliente N°:{self.cliente}\nNome:{self.nome} \nCPF:{self.cpf}\nSaldo em conta após processo realizado:{self.saldo}\n")


def main():
    c1 = Conta1(12, "123.456.789-10", "João", 0)
    c1.depositar(350)   # Valor de um depósito aleatório
    c1.sacar(100)   # Valor de um saque aleatório
    c1.valor_em_conta()

# Quando um script python é executado, a variável reservada NAME referente a ele tem valor igual a "__main__". Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso, é um chamado ao método main do script


if __name__ == "__main__":
    main()