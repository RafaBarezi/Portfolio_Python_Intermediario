# Implementar uma solução que calcule as raízes de uma equação do segundo grau:

# X² + 5x + 6 = 0  As raízes são {-3 e -2} Ela não tem raíses nos números reais.

import numpy as np

def entrada_dados():
    coeficiente = quantidade = int(input("Digite o valor do coeficiente >>> "))
    return coeficiente

def calc_delta(a, b, c):
    delta = (b*b)-4*a*c
    return delta

def calcular_raizes(a, b, c, delta):
    if (delta < 0):
        resultado = "A equação não possui raízes nos números reais"
    elif (delta == 0):
        x = - b/(2*a)
        resultado = f"A equação possui somente a raiz {x}"
    else:
        x1 = (-b-np.sqrt(delta))/(2*a)
        x2 = (-b+np.sqrt(delta))/(2*a)
        resultado = f"A equação possui as raízes : {x1} e {x2}"
    return resultado

# f(x)= ax²+bx+c

a = entrada_dados()
b = entrada_dados()
c = entrada_dados()

delta = calc_delta(a, b, c)

resultado = calcular_raizes(a, b, c, delta)
print(resultado)