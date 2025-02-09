# Formatação saída

print("\n")
hora = 10
minutos = 26
segundos = 18
print(f"{hora}:{minutos}:{segundos}")
print("{}:{}:{}". format(hora, minutos, segundos))
print("\n")

"""
O método format() também pode ser usado para imprimir valores de ponto flutuante com a precisão definida. Vamos a mais um exemplo:
Ao usar {:8.5}, estamos determinando que a impressão será com 8 espaços, mas apenas 5 serão utilizados.

Para sequencias podemos fazer da seguinte forma:

"""

seq = [0, 1, 2, 3, 4, 5]
print(seq)

"""
Para imprimir uma substring, por exemplo, basta utilizar os colchetes para indicar o intervalo de índices que deve ser impresso. Vale lembrar que o primeiro caractere da string é indexado com 0:
"""
str = "Hello World"
print(str[0:4])
print(str[3:8], "\n")

# Também é possível imprimir a string como lida da direita para a esquerda. Para isso, deve-se utilizar [: : -1]. Esse valor -1 indica que a leitura dos caracteres será feita no sentido oposto ao tradicional:

print(str[::-1])
print(str[8:2:-1],"\n")