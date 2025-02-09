import datetime

class Conta_Poupança:
    def __init__(self, taxa_remuneracao):
        self.taxa_remuneracao = taxa_remuneracao
        self.data_abertura = datetime.datetime.today()

    def Remuneracao_Conta(self):
        saldo.saldo += self.saldo * self.taxa_remuneracao # type: ignore

class Conta_Cliente:
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valor_investido = valor_investido
        self.taxa_rendimento = taxa_rendimento

    def Calculo_Rendimento(self):
        self.valor_investido += (self.valor_investido * self.taxa_rendimento)
        self.valor_investido = (self.valor_investido -
                                (self.taxa_rendimento * self.IOF * self.IR))

    def Extrato(self):  
        print(
            f"\nO saldo atual da Conta {self.numero} é R$ {self.valor_investido:10.2f}\n")

class Conta_Comum(Conta_Cliente):
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)

    def Calculo_Rendimento(self):  
        self.valor_investido += (self.valor_investido * self.taxa_rendimento)

class Banco():

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def Adiciona_Conta(self, Conta_Cliente):
        self.contas.append(Conta_Cliente)

    def Calcular_Rendimento_Mensal(self):  
        for c in self.contas:
            c.Calculo_Rendimento()

    def Imprime_Saldo_Contas(self):
        for c in self.contas:
            c.Extrato()

class Conta_Remunerada(Conta_Cliente):
    def __ini__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)

    def Calculo_Rendimento(self):  
        self.valor_investido += (self.valor_investido * self.taxa_rendimento)
        self.valor_investido -= (self.valor_investido * self.IOF)

banco_01 = Banco("0001", "Banco Teste")
conta_cliente_01 = Conta_Cliente("0001", 0.01, 0.1, 1000, 0.05)
conta_comum_1 = Conta_Comum("0002", 0.01, 0.1, 2000, 0.05)
conta_remunerada_01 = Conta_Remunerada("0003", 0.01, 0.1, 2000, 0.05)

banco_01.Adiciona_Conta(conta_cliente_01)  
banco_01.Adiciona_Conta(conta_comum_1)  
banco_01.Adiciona_Conta(conta_remunerada_01)  
banco_01.Calcular_Rendimento_Mensal()  
banco_01.Imprime_Saldo_Contas() 