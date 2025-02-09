# Procedimentos: São aqueles que não retornam valores. / Funções: São aquelas que retornam valores.

# função não possui qualquer retorno, possui comportamento de procedimento.
def func1(x):
    x = 10
    print(f'\nFunção func1 - x = {x}')

# função não possui qualquer retorno, possui comportamento de procedimento.
def func2(x):
    x = 20
    print(f'\nFunção func2 - x = {x}')

x = 0
func1(x)
func2(x)
print(f'\nPrograma principal - x = {x}\n')