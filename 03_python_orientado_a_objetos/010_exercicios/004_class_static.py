from datetime import date

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Um método de classe para criar um objeto Pessoa através do ano de nascimento:

    @classmethod
    def a_partir_ano_nascimento(cls, nome, ano):  # cls cria classe
        return cls(nome, date.today().year - ano)

# Método estático para verificar se é maior de idade:

    @staticmethod  # Não usa __init__ nem cls, não é ligado a um objeto, ele é geral
    def maior_idade(outra_idade):
        return outra_idade >= 18

pessoa1 = Pessoa("Rafaela", 35)
pessoa2 = Pessoa.a_partir_ano_nascimento("Mel", 2019)

print()
print(pessoa1.idade)
print(pessoa2.idade)
print(Pessoa.maior_idade(17))
print()