valor = 20

# A função multiplica desse script não é pura, pois além de não depender apenas dos parâmetros, ela não retorna valor algum:

def multiplica(fator):
    global valor
    valor = valor * fator
    print("\nResultado >>> ", valor)

def main():
    # esta é a instrução pass
    numero = int(input("\nPor favor, digite um n° >>> "))
    multiplica(numero)
    multiplica(numero)
    print()

# Ou podemos tentar sem a instrução pass, usando a entrada como 3, por exemplo:

# def main():
#     multiplica(3)
#     multiplica(3)
#     print()

if __name__ == "__main__":
    main()
