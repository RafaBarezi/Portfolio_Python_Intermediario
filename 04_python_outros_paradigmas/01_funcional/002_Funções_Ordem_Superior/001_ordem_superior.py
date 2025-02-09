# Na programação funcional, é muito comum utilizar funções que aceitem outras funções, como parâmetros ou que retornem outra função. Estas são chamadas de funções de ordem superior (higher order function).

def multiplicar_por(multiplicador): # Função pai 
    def multi(multiplicando):
        return multiplicando * multiplicador
    return multi

a = int(input("\nDigite um n° >>> "))
b = int(input("Digite um n° >>> "))

def main():
    multiplicar_por_2 = multiplicar_por(2) # Referência para a função multi recém-criada.
    print("\nMultiplicando os n°s digitados por 2:\n")
    print(multiplicar_por_2(a))
    print(multiplicar_por_2(b))

    multiplicar_por_5 = multiplicar_por(5) # Referência para a função multi recém-criada.
    print("\nMultiplicando os n°s digitados por 5:\n")
    print(multiplicar_por_5(a))
    print(multiplicar_por_5(b))

if __name__ == "__main__":
    main()