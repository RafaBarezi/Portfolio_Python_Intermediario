# Esse é um tipo de classe que não pode ser instanciado durante a execução, ou seja, não pode haver objetos dessa classe executados na memória.

# O Python utiliza um módulo chamado abc para definir uma classe como abstrata, a qual será herdeira da superclasse ABC

# Toda classe abstrata é uma subclasse da classe ABC. Para tornar a classe Conta Cliente abstrata, muda-se sua definição para:

# O decorator @abstractmethod indica para a linguagem que o método é abstrato

from abc import ABC, abstractmethod

class ContaCliente(ABC):
    def __init__(self, numero, IOF, IR, Valor_Investido, Taxa_Rendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.Valor_Investido = Valor_Investido
        self.Taxa_Rendimento = Taxa_Rendimento

    @abstractmethod
    def Calculo_Rendimento(self):
        pass

cc1 = ContaCliente(1, 0.1, 0.25, 0.1)

# Quando se tentar instanciar um objeto da classe, será obtido um erro indicando que essa classe não pode ser instanciada, por isso o erro

# As classes mencionadas devem obrigatoriamente implementar os métodos. Caso contrário, elas serão classes abstratas e delegarão para as suas subclasses a implementação concreta do método abstrato.