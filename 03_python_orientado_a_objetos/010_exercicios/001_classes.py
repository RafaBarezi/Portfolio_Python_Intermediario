# Fazendo uma classe no Python:

class Familia:
    def __init__(self, nome, idade):
        # _init é o construtor
        # Self é um parâmetro de auto-referência
        self.set_nome(nome)
        self.set_idade(idade)
        # Usamos o set para tornar ele um atributo da classe

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

# Criando um objeto (Instanciando a classe):
familiar1 = Familia("Rafaela ", "35 anos")
familiar2 = Familia("Mãe", "50 anos")
familiar3 = Familia("Pai", "54 anos")
familiar4 = Familia("Irmão", "22 anos")
familiar5 = Familia("Mel Shih Tzu", "3 anos")

# Imprimir um objeto:
print(f"\nNome: {familiar1.get_nome()}\nIdade: {familiar1.get_idade()}")
print(f"\nNome: {familiar2.get_nome()}\nIdade: {familiar2.get_idade()}")
print(f"\nNome: {familiar3.get_nome()}\nIdade: {familiar3.get_idade()}")
print(f"\nNome: {familiar4.get_nome()}\nIdade: {familiar4.get_idade()}")
print(f"\nNome: {familiar5.get_nome()}\nIdade: {familiar5.get_idade()}")
print()
