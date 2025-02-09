# A função map é utilizada para aplicar uma determinada função em cada elemento de um iterável (lista, tupla, dicionários etc.), retornando um novo iterável com os valores modificados

# A função map é pura e de ordem superior, pois depende apenas de seus parâmetros e recebe uma função como parâmetro. A sua sintaxe é a seguinte: map(função, iterável1, iterável2...)

lista = [1, 2, 3, 4, 5]

def triplica(item):
    return item * 3

def main():
    print("\nLista original", list(lista))
    nova_lista = map(triplica, lista)
    print("\nNova lista multiplicada por 3:",list(nova_lista),"\n")

if __name__ == "__main__":
    main()  

# A função map garante a imutabilidade dos iteráveis passados como argumento. Como a função map retorna um iterável, utilizamos o construtor list (iterável).