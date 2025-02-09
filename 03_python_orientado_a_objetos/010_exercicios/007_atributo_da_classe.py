# Métodos que se comportam fora da classe:

class Nome_Completo:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    # ganha referencia para a classe, podendo criar padrão fábrica (facytory)
    @classmethod
    def fromString(cls, texto):  # cls é Nome_Completo
        # map  significa mapeando para nome e sobrenome
        nome, sobrenome = map(str, texto.split(" "))
        objeto = cls(nome, sobrenome)
        return objeto  # vai retornar o nome do objeto com a classe

registro_1 = Nome_Completo.fromString("Joao Silva")