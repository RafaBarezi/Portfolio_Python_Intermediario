class Pessoa:
    def __init__(self, nome, idade):  # _init_ é o construtor, inicializa os objetos
        self.nome = nome
        self.idade = idade

    def imprimir(self):
        print(self.nome, "tem", self.idade, "anos.")

    # gettering e setering promovem o encapsulamento

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

# Veremos um exemplo de polimorfismo , onde vemos o pai mostrando nome e idade e o filho mostrando a profissão

class Profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        # Atenção ao underline duplo
        super().__init__(nome, idade)
        self.profissao = profissao

    def imprimir(self):
        super().imprimir()
        print("Trabalha como", self.profissao)

prof = Profissional("\nRafaela Barezi", 35,
                    "analista de sistemas e consultora em marketing digital\n")
prof.imprimir()