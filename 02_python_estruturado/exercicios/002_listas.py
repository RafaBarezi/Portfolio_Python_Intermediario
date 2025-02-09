# Implementar uma solução que some todos os pares de uma lista ( se a lista for {10, 2, 5, 7, 6 e 3} tem que dar 18)

lista = [2, 3, 35, 18, 9]
soma = 0
for num in lista:
    if (num % 2 == 0):
        soma = soma + num
print(f"\nO somatório dos elementos pares da lista é {soma}")