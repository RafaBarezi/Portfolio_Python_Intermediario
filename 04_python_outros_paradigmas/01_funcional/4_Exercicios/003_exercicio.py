# Arredondar os valores da lista 

lista_numeros = [9.56789, 8.45678, 7.34567, 6.23456, 5.1234]

lista_precisao = [2, 2, 3, 3] # deixar os 2 primeiros n°s com 2 casas e os últimos com 3

arredondamento = lambda x, y: round(x, y)

resultado = list(map(arredondamento, lista_numeros, lista_precisao))

print(resultado,"\n")