# Referências entre objetos I

from Conta1 import Conta1

cliente_1 = Conta1("N° da conta 123", "123.456.789-10", "Joao", 120)
cliente_2 = Conta1("N° da conta 124", "123.123.789-10", "Maria", 0)
cliente_3 = Conta1("N° da conta 125", "123.456.123-10", "Ana", 167)
cliente_4 = Conta1("N° da conta 126", "123.456.123-12", "Carlos", 321)
cliente_5 = Conta1("N° da conta 127", "345.456.789-10", "Paulo", 43)

print()
print(cliente_1.cpf)
print(cliente_2.cpf)
print(cliente_3.cpf)
print(cliente_4.cpf)
print(cliente_5.cpf)

if (cliente_1.cpf != cliente_2.cpf != cliente_3.cpf != cliente_4.cpf != cliente_5.cpf):
    print("\nNão existem cadastros duplicados\n")
else:
    print("\nExistem cadastros duplicados\n")