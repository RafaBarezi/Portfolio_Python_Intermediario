# Não existe a obrigatoriedade da instanciação de um objeto da classe.

import math

class Math:

    @staticmethod
    def sqrt(x):
        return math.sqrt(x)

print(Math.sqrt(4))
print(Math.sqrt(9))
print(Math.sqrt(16))
print(Math.sqrt(25))
print(Math.sqrt(36))
print(Math.sqrt(49))

# No caso acima, o método sqrt da classe Math foi chamado sem que um objet da classe Math fosse instanciado.

# Os métodos estáticos não são uma boa prática na programação orientada a objetos. Eles devem ser utilizados apenas em casos especiais.