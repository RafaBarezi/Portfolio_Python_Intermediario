# Filter é utilizada para filtrar elementos de um iterável (lista, tupla, dicionários etc.). O filtro retorna true ou false (verdadeiro ou falso) para cada elemento do iterável. Sua sintaxe é: filter(função, iterável)

lista = [1, 2, 3, 4, 5]

def impares(iterable):  # recebemento um iterável como parâmetro
    lista_aux = []  # criação de lista auxiliar para garantir imutabilidade
    for item in iterable:
        if item % 2 != 0:
            # Função adiciona os itens ímpares à lista auxiliar
            lista_aux.append(item)
    return lista_aux

def main():
    nova_lista = impares(lista)
    print("\n", nova_lista, "\n")

if __name__ == "__main__":
    main()