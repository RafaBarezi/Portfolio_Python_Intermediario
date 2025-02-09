# Classe Círculo com atributo de classe privado

from Circulo import Circulo

circulo1 = Circulo(1, 1, 10)
print(circulo1._total_circulos)

circulo2 = Circulo(2, 2, 20)
print(circulo2._total_circulos)

print(Circulo.total_circulos)