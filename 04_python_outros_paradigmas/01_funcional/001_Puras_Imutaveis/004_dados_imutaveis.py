# Na programação funcional, devemos tratar todos os dados como imutáveis! Devemos também evitar alterar qualquer dado que já tenha sido criado.

valores = input(
    "\nInforme 3 números (separe-os com espaços, não com vírgulas) >>> ")

# Passamos a lista valores como argumento para a função altera_lista. No Python, ao passar uma lista como argumento, apenas passamos sua referência, portanto qualquer mudança feita no parâmetro dentro da função, também altera a lista original.

# separando os valores pelo espaço em branco e transformando-os em uma lista de inteiros
valores = [int(i) for i in valores.split()]

def altera_lista(lista):
    nova_lista = list(lista)# ao invés de alterarmos o valor do próprio parâmetro, criamos uma cópia dele sendo assim, não alteramos a variável.
    nova_lista[2] = lista[2] + 10
    return lista

def main():
    print("\nLista original:", valores)
    print("Lista 1:", altera_lista(valores))
    print("Lista 2:", altera_lista(valores), "\n")

if __name__ == "__main__":
    main()

# As funções puras e dados imutáveis buscam evitar os efeitos indesejáveis, como ocorreu no script anterior. Na terminologia de programação funcional, chamamos isso de efeito colateral (side effect). 
