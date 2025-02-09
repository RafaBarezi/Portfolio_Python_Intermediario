# Classes e objetos - Composição

import datetime
from Conta4 import Conta4
from Extrato import Extrato
from Cliente import Cliente

cliente1 = Cliente("Joao", "Rua 1", 100)
cliente2 = Cliente("Maria", "Rua 2", 200)
cliente3 = Cliente("José", "Rua 3", 150)
cliente4 = Cliente("Ana", "Rua 4", 400)

conta_corrente_1 = Conta4([cliente1, cliente2], "001",
                          cliente1.saldo + cliente2.saldo)

conta_corrente_1.depositar(1500)
conta_corrente_1.extrato.extrato(conta_corrente_1.numero)
conta_corrente_1.gerarsaldo()

print("\n----------------------------------")

conta_corrente_2 = Conta4([cliente3, cliente4], "002",
                          cliente3.saldo + cliente4.saldo)

conta_corrente_2.sacar(50)
conta_corrente_2.extrato.extrato(conta_corrente_2.numero)
conta_corrente_2.gerarsaldo()

print("\n----------------------------------")

conta_corrente_1 = Conta4([cliente1, cliente2], "001",
                          cliente1.saldo + cliente2.saldo + conta_corrente_1.saldo)

conta_corrente_1.transfereValor(conta_corrente_1, 300)
conta_corrente_1.extrato.extrato(conta_corrente_1.numero)
conta_corrente_1.gerarsaldo()

print("\n----------------------------------")