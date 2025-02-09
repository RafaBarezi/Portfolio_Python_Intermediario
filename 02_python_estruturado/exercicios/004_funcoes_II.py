# Implementar uma solução que retorne a soma de todos elementos pares de uma lista:

def paridade(num):
    resto = (num % 2 == 0)
    return resto

def somar_par(lista):
    soma = 0
    for num in lista:
        if (paridade(num)):
            soma = soma + num
    return soma

lista = [10, 2, 5, 7, 6, 3]
soma = somar_par(lista)
print(f"\nO somatório dos n°s pares da lista é {soma}\n")