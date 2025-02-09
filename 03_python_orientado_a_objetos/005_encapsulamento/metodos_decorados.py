# métodos decorados com @property e @< nomedometodo >.setter

class Conta:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo inválido")
        else:
            self._saldo = saldo

def main():
    conta = Conta("001")
    conta.saldo = 1000  # usando o @saldo.setter
    print(f'\nNúmero da conta >>> {conta.numero} \nsaldo da conta = {conta.saldo}\n') # usando o @property

if __name__ == "__main__":
    main()