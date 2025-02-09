# A sequência de Fibonacci é: 1, 1, 2, 3, 5, 8, 13, 21... Os dois primeiros termos são 1; a partir do 3º termo, cada termo é a soma dos dois anteriores.

def fibonacci(n):
    if n == 1 or n == 2: # definida as condições de parada
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) # definindo as chamadas recursivas para calcular os dois termos anteriores da sequência.