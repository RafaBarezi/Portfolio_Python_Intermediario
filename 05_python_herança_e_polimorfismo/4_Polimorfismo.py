# Polimorfismo I:

# Primeiro criamos as classes:

class Argentina():
    def capital(self):
        print("\nBuenos Aires é a capital da Argentina")

    def lingua_oficial(self):
        print("O espanhol é a lingua oficial da Argentina")

class Brasil():
    def capital(self):
        print("Brasilia é a capital do Brasil")

    def lingua_oficial(self):
        print("O português é a língua oficial do Brasil\n")

# Depois criamos os objetos Argentina e Brasil:

obj_arg = Argentina()
obj_bra = Brasil()

for pais in (obj_arg, obj_bra):
    pais.capital()
    pais.lingua_oficial()

# Polimorfismo II:

class Maça():
    def Nome(self):
        print("\nMaça")

    def Cor(self):
        print("Vermelho")

    def Sabor(self):
        print("Doce")

class Pera():
    def Nome(self):
        print("\nPera")

    def Cor(self):
        print("Amarelo")

    def Sabor(self):
        print("Doce")

class Uva():
    def Nome(self):
        print("\nUva")

    def Cor(self):
        print("Roxo")

    def Sabor(self):
        print("Doce")

class Kiwi():
    def Nome(self):
        print("\nKiwi")

    def Cor(self):
        print("Verde")

    def Sabor(self):
        print("Azedo\n")

obj_maça = Maça()
obj_pera = Pera()
obj_uva = Uva()
obj_kiwi = Kiwi()

for fruta in (obj_maça, obj_pera, obj_uva, obj_kiwi):
    fruta.Nome()
    fruta.Cor()
    fruta.Sabor()

# Polimorfismo III:

class Veículo:
    def rodar(self):
        print("\nReduz o consumo de combustível")

class Veículo_Elétrico(Veículo):
    def rodar(self):
        super().rodar()  # super faz referência ao construtor da classe mãe, ao método rodar
        print("\nEste veículo usa eletricidade\n")

veiculo_eletrico = Veículo_Elétrico()  # objeto instanciando a Classe
veiculo_eletrico.rodar()

# Exceção:

# Para subir uma exceção com uma mensagem, quando é preciso forçar um erro:

#x = 10
#if x > 5:
#   raise Exception("x não pode ser maior que 5. O valor de x é {}".format(x))