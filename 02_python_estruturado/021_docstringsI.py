# É possível definir uma string que serve como documentação de funções definidas pelo desenvolvedor. Ao chamar o utilitário help() passando como parâmetro a função desejada, essa string é exibida.

def Fibonacci(n):

    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

"Determina o n-ésimo termo da sequência de Fibonacci:"

print(help(Fibonacci),"\n")