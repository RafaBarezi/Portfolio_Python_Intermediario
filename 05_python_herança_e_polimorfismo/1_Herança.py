# Herança:

class ClasseSomaMultiplica:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a+self.b

    def multiplicar(self):
        return self.a*self.b

class Derivada(ClasseSomaMultiplica):
    def subtrair(self):
        return self.a-self.b

    def Dividir(self):
        return self.a/self.b

d = Derivada(30, 20)

print(f"\nA soma de 30 e 20 é {d.somar()}")
print(f"A diferença de 30 e 20 é {d.subtrair()}")
print(f"A multiplicação de 30 e 20 é {d.multiplicar()}")
print(f"A divisão de 30 e 20 é {d.Dividir()}\n")
# Aqui estamos testando se uma classe é derivada ou não
print(issubclass(Derivada, ClasseSomaMultiplica))

# Sobrecarga:

# Sobrecarga é um passo antes do polimorfismo

def somar(x, y, z=0):  # Se não passar o terceiro parâmetro, ele será 0
    return x + y + z

print("\n",somar(10, 20))
print(somar(10, 20, 30))