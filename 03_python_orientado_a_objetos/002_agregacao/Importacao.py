# Referências entre objetos II

from Conta2 import Conta2

contaA = Conta2("N° da conta 123", "123.456.123-10", "Ana", 100)
contaB = Conta2("N° da conta 124", "456.123.789-10", "Maria", 250)
contaA.depositar(1000)
contaA.transfereValor(contaB, 500)
print(
    f"\nA conta da Ana tinha R$ 100, depois de depositar R$ 1000 e transferir R$ 500, fica com RS{contaA.saldo}.\n")
print(
    f"A conta da Maria tinha R$ 250. Depois da transferência fica com RS {contaB.saldo}.\n")