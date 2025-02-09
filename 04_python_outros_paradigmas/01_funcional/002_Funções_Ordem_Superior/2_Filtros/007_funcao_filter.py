lista = [1, 2, 3, 4, 5]

def impar(item):  # Definimos a função ímpar, que retorna true se o item passado como parâmetro é ímpar ou false caso contrário
    return item % 2 != 0

def main():
    nova_lista = filter(impar, lista)
    # O resultado da função filter é armazenado na variável nova_lista, para então ser impresso
    print("\n", nova_lista, "\n")

if __name__ == "__main__":
    main()