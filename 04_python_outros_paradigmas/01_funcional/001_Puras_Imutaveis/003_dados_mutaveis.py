valores = input("\nInforme 3 números (separe-os com espaços, não com vírgulas) >>> ") 

valores = [int(i) for i in valores.split()] 

def altera_lista(lista):
    lista[2] = lista[2] + 10 # Aqui alteramos também a variável global valores. Com isso, ao chamar a mesma função duas vezes, obtemos um efeito indesejável, resultando em saídas diferentes.
    return lista

def main():
    print("\nLista original:", valores)
    print("Lista 1:", altera_lista(valores))
    print("Lista 2:", altera_lista(valores),"\n")

if __name__ == "__main__":
    main()