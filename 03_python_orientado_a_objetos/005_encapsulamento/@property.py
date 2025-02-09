# Utilizando o decorator property nos métodos, mantém-se os atributos como protegidos, os quais, por sua vez, são acessados apenas por meio dos métodos “decorados” com property

from Conta5 import Conta5 

@property
def saldo(self):
    return self._saldo

# Os properties ajudam a garantir o encapsulamento no Python