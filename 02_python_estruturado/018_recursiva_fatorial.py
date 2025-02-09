# Fatorial :   N! = n.(n-1)  ex: 5!=5.4.3.2.1= 120 *Obs: Para o calculo de 0! ou 1! O resultado é 1.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1)