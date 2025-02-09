lista = [1, 2, 3, 4, 5]

nova_lista = map(lambda item: item * 3, lista) # Substituímos a função triplica pela função lambda,  esta vai aplicar a função lambda em cada item da lista, retornando um novo iterável impresso. 

def main():
    print("\nLista original", list(lista))
    print("\nNova lista multiplicada por 3:",list(nova_lista),"\n")

if __name__ == "__main__":
    main()

# Observe como o código foi reduzido e mesmo assim preservamos a utilização de funções puras (lambda), alta ordem (map) e que preservaram a imutabilidade dos dados. Tudo isso para garantir que não haja efeitos colaterais, (quando a função faz alguma operação que não seja computar a saída a partir de uma entrada) e dependência de estados.