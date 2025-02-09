# Paradigma funcional repetindo o exemplo anterior:

print("\nPrimeiro exemplo:")

def sum(numeros):
    if not numeros:
        return 0
    valores = numeros[0]
    valor = numeros[1:]
    return valores + sum(valor)

print(sum([2, 4, 6, 8]))

print("\nSegundo exemplo:")
import operator
lista = ["Ferrari"]
nova_lista = lista + ["Porsche"]
print(nova_lista)

print("\nTerceiro exemplo:")
print(operator.add(10, 20))

print("\nQuarto exemplo")
from functools import reduce
print(reduce(operator.add, [10, 30]))
print(reduce(operator.concat, ["Aprendendo reduce"]), "\n")