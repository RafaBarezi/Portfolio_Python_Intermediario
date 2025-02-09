# Implementar uma solução que calcule o fatorial de um n°:

# Fatorial :   N! = n.(n-1)  ex: 5!=5.4.3.2.1= 120 *Obs: Para o calculo de 0! ou 1!o resultado é 1.

#  Estratégia 01
def fatorial_iterativo(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

#  Estratégia 02
def fatorial_recursivo(n):
    if (n == 0) or (n == 1):
        return 1
    return n * fatorial_recursivo(n-1)

numero = eval(input("Por favor, digite um número: "))
print(f"O fatorial de {numero} é:{fatorial_iterativo(numero)}")
print(f"O fatorial de {numero} é:{fatorial_recursivo(numero)}")