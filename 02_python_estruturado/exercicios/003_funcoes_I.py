# Implementar uma solução que retorne o menor elemento de uma lista:

def encontrar_minimo(lista):
    minimo = lista[0]
    for elemento in lista:
        if (elemento < minimo):
            minimo = elemento
    return minimo

lista_teste = [2, 10, 3, 1, 4, 5]
menor = encontrar_minimo(lista_teste)
print("\nO menor número da lista é: {}\n".format(menor))