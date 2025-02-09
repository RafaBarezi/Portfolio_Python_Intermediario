# Uma função recursiva é aquela que chama a si mesma.

def regressiva(x):
    print(x)
    regressiva(x - 1)

# Conceitualmente, essa execução será repetida indefinidamente até que haja algum erro por falta de memória. Perceba que não definimos adequadamente uma condição de parada para a função regressiva(), o que leva a esse comportamento ruim.