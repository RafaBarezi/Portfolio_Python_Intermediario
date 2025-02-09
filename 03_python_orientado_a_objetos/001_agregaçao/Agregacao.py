# Agregação classes Dados_Cliente e Conta3

from Cliente import Cliente
from Conta3 import Conta3

cliente1 = Cliente(123, "Joao", "Rua 1", 400)
cliente2 = Cliente(345, "Maria", "Rua 2", 200)
cliente3 = Cliente(345, "Ana", "Rua 3", 300)
cliente4 = Cliente(345, "Pedro", "Rua 4", 260)
cliente5 = Cliente(345, "Carlos", "Rua 5", 320)

conjunta1 = Conta3([cliente1, cliente2], "001",
                   (cliente1.saldo + cliente2.saldo))

# Na linha número 12, é instanciado um objeto conjunta com dois clientes agregados: cliente1 e cliente2. Esses dois objetos são passados como parâmetros.

print("\n----------------------------------\n")

conjunta1.deposito(1500)
conjunta1.saque(500)
conjunta1.extrato()

print("\n----------------------------------")

conjunta2 = Conta3([cliente3, cliente4, cliente5], "002",
                   (cliente3.saldo + cliente4.saldo + cliente5.saldo))

conjunta2.deposito(500)
conjunta2.extrato()
print()