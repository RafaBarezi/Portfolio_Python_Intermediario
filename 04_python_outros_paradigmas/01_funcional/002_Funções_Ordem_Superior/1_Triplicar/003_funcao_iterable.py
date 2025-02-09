lista = [1, 2, 3, 4, 5]

def triplica_itens(iterable):  # iterável como parâmetro
    lista_aux = []  # criação de lista auxiliar para garantir imutabilidade
    for item in iterable:
        # adição de itens triplicados à lista auxiliar
        lista_aux.append(item*3)
    return lista_aux

def main():
    nova_lista = triplica_itens(lista)
    print("\n", nova_lista, "\n")

if __name__ == "__main__":
    main()