# Implementar uma solução que retorne os número primos:

def primos(num):
    if (num < 2):
        return False
    i = num//2
    while (i > 1):
        if (num % i == 0):
            return False
        i = i - 1
    return True

def imprimir_resultado(numero, resultado):
    mensagem = f"\nO número {numero} não é primo\n"
    if (resultado):
        mensagem = f"\nO número {numero} é primo\n"
    return mensagem

numero = eval(input("\nPor favor, digite um número: "))
resultado = primos(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)