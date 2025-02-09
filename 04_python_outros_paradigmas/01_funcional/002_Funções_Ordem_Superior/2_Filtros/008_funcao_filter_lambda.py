lista = [1, 2, 3, 4, 5]

# Substituímos a função ímpar pela função lambda (em comparação com o script anterior) que foi utilizada como argumento para a função filter. Esta vai aplicar a função lambda em cada item da lista.
nova_lista = filter(lambda item: item % 2 != 0, lista)

def main():
    print("\n", list(nova_lista), "\n")

if __name__ == "__main__":
    main()