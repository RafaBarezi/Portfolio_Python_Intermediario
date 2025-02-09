escolha = input("\nEscolha uma opção de função: 1 ou 2 >>> ")

if escolha == "1": # se digitar 1 obtemos o resultado de 1 + 10
    def func_01(x):
        return x + 1
    s = func_01(10)
else:
    def func_02(x): # se digitar 2 obtemos o resultado de 2 + 20
        return x + 2
    s = func_02(20)

print("\n", s, "\n")