# As variáveis locais podem ser: dinâmicas da pilha (vinculadas ao armazenamento no início da execução) ou estáticas (vinculadas ás células de memória)

# Para alterar a variável global x, seria necessário explicitar, dentro de cada função, que o nome x é referente a ela. Isso pode ser feito com a palavra reservada global. Além de explicitar a referência à variável global, as funções func1(x) e func2(x) não recebem mais os parâmetros de mesmo nome, já que fazem referência à variável global:

def func1():
    global x
    x = 10
    print(f'\nFunção func1 - x = {x}')

def func2():
    global x
    x = 20
    print(f'\nFunção func2 - x = {x}')

x = 0
func1()
func2()
print(f'\nPrograma principal - x = {x}\n')