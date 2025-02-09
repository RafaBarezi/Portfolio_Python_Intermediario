# Agregação, classes e métodos estáticos (parte 2)

# Atributos estáticos (O que você define fora do init)

class Pessoa:
    _contador = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa._contador += 1  # Contador da classe não do objeto

    def imprimir(self):
        print(self.nome, "tem", self.idade, " anos\n")

    @property  # decoração, ou seja, metadados associadaos á classe
    def contador(self):
        return type(self)._contador

p1 = Pessoa("\nCarlos", 18)
p2 = Pessoa("Ana", 28)
p3 = Pessoa("Maria", 9)

print(p1.nome)
print(p2.nome)
print(p3.nome)

# Podemos jogar o contador das seguintes formas:
print("\nExistem", Pessoa._contador, "pessoas cadastradas")  # ou:
print("\nExistem", p1._contador, "pessoas cadastradas\n")