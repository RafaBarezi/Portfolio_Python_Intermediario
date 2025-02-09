# Os métodos decorados com a property @setter forçam todas alterações de valor dos atributos privados a passar por esses métodos.

# Notação: @< nomedometodo >.setter

from Conta5 import Conta5


@saldo.setter # type: ignore
def saldo(self, saldo):
    if (self.saldo < 0):
        print("saldo inválido")
    else:
        self._saldo = saldo