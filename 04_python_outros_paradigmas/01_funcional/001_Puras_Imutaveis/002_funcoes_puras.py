# Funções puras:

valor = 20

# A função multiplica desse script é pura, pois depende apenas dos próprios parâmetros para gerar resultados, ela  retorna valor e não acessa ou modifica nenhuma variável externa:

def multiplica(valor, fator):
    valor = valor * fator
    return valor

def main():
    numero = int(input("\nPor favor, digite um número >>> "))
    print("\nResultado >>> ", multiplica(valor, numero))
    print("\nResultado >>> ", multiplica(valor, numero))
    print()

# Ou podemos tentar sem a instrução pass, usando a entrada como 3, por exemplo:

# def main():
#     numero = 3
#     print("\nResultado", multiplica(valor, numero))
#     print("Resultado", multiplica(valor, numero))
#     print()

if __name__ == "__main__":
    main()
