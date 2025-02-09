# Classe Salário

class Salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base*12)+(self.bonus)

# Classe Empregado

class Empregado(Salario):
    # O self só serve para referência dentro da classe / salario é apenas uma instância da classe Salario
    def __init__(self, nome, idade, profissao, salario):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.salario_agregado = salario  # Agregação

    def salario_total(self):
        return self.salario_agregado.salario_anual()

salario = Salario(10000, 700)
empregado = Empregado("Musashi", 46, "analista", salario)
print("\n", empregado.salario_total(), "\n")