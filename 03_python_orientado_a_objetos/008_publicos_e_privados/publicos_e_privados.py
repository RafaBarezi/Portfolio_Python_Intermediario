# Métodos públicos e privados

# O método pode ser declarado como privado, mesmo que ainda possa ser chamado diretamente como se fosse um método público.

# Os dois underscores antes do método indicam que ele é privado:

class Circulo:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    def _gerarsaldo(self):
        print(f"Numero: {self.numero}\n Saldo:{self.saldo}")

# No código acima, foi definido o método __gerarsaldo como privado. Portanto, ele pode ser acessado apenas internamente pela classe Conta