# o Python permite a criação de funções anônimas. Estas são definidas sem identificador (ou nome) e, normalmente, são utilizadas como argumentos para outras funções (de ordem superior).

# As funções anônimas são chamadas de funções lambda. Para criá-las, utilizamos a seguinte sintaxe:  lambda argumentos: expressão

def multiplicar_por(multiplicador):
    return lambda multiplicando: multiplicando * multiplicador

# Verificar no exemplo Ordem_superior. Trocamos o multi por lambda

# Não esquecer do return

a = int(input("\nDigite um n° >>> "))
b = int(input("Digite um n° >>> "))

def main():
    # Referência para a função multi recém-criada.
    multiplicar_por_2 = multiplicar_por(2)
    print("\nMultiplicando os n°s digitados por 2:\n")
    print(multiplicar_por_2(a))
    print(multiplicar_por_2(b))

    # Referência para a função multi recém-criada.
    multiplicar_por_5 = multiplicar_por(5)
    print("\nMultiplicando os n°s digitados por 5:\n")
    print(multiplicar_por_5(a))
    print(multiplicar_por_5(b))

if __name__ == "__main__":
    main()

# Na programação funcional é não se deve utilizar laços (for e while), mas sim composição de funções ou recursividade. A função lambda exerce um papel fundamental nisso.

# As funções internas mais comuns são map e filter.