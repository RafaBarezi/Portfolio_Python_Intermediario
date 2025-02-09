# Deixar palavras com letras minúsculas

veiculos = ["aviao", "carro", "navio", "onibus", "bicicleta"]

print("\n", f"Nomes minúsculos = {veiculos}")

# palavra chave lambda, parâmetro x. Aqui ela recebe x e converte para maiúscula
def f_maiuscula(x): return str.upper(x)

# fazendo mapeamento para cada uma das funções da lista / O list serve para transformar o objeto criado em uma lista
nomes_maiusculos = list(map(f_maiuscula, veiculos))

print("\n", f"Nomes maiúsculos = {nomes_maiusculos}", "\n")