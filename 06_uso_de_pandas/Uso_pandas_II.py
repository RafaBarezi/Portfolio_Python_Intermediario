import pandas as pd

# Criando o conjunto de dados
dataset = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]
colunas = ["a", "b", "a e b", "a ou b"]
ordf = pd.DataFrame(dataset, columns=colunas)

# Exportando o DataFrame para um arquivo CSV
ordf.to_csv("ordf.csv", index=False)  # O parâmetro index=False evita salvar o índice no CSV

# Lendo o arquivo CSV de volta
lendo_o_ativo_de_dados = pd.read_csv("ordf.csv")

# Exibindo o conteúdo do DataFrame lido
print("\n",lendo_o_ativo_de_dados)

# Verificando as colunas e os valores
print("\n",lendo_o_ativo_de_dados.columns)
print("\n",lendo_o_ativo_de_dados.values)

# Lendo o CSV em outro DataFrame (exemplo1)
exemplo1 = pd.read_csv("ordf.csv")
print("\n",exemplo1)