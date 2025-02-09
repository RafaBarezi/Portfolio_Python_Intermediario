import datetime

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

    def gerarsaldo(self):
        print(f"\nO saldo atual da sua conta é de R${self.saldo}")

# O método __Init__ foi sobrescrito da superclasse Conta. Já o método super(), que foi utilizado para chamar um método da superclasse, pode ser usado em qualquer método da subclasse:

class Conta_Especial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        # Podemos usar super() no lugar no _init_, exceto quando se tratar de uma herança multipla
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

# Conta Especial reescreveu o método sacar da superclasse Conta. Essa característica é conhecida como sobrescrita (override) dos métodos

# Ele é uma classe comum e pode ser instanciada como todas as outras classes independentes da instanciação de objetos da classe Conta.

    def Sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["SAQUE", valor, "data", datetime.datetime.today()])
            return True

cliente_1 = Cliente("João", "Rua A", 1000.00)
cliente_2 = Cliente("Maria", "Rua B", 1000.00)
cliente_3 = Cliente("Ana", "Rua C", 1000.00)
conta1 = Conta([cliente_1, cliente_2], "004",
               cliente_1.saldo + cliente_2.saldo)
conta2 = Conta_Especial([cliente_3], "005", cliente_2.saldo, 2000)
conta2.depositar(100)
conta2.sacar(3200)
# Valor do saque 3200.00 maior que o valor do saldo mais o limite 3100.00
conta2.extrato.extrato(conta2.numero)