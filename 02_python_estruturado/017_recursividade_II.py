# o interpretador pode interromper a execução indefinida, mas essa não é uma boa prática. Uma forma de contornar esse problema é definir adequadamente uma condição de parada:

def regressiva(x):
    if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva(x-1)