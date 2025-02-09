# Os métodos de classe são a maneira indicada para se acessar os atributos de classe. Eles têm acesso diretamente à área de memória que contém os atributos de classe.

# Para definir um método como estático, deve-se usar o decorator @classmethod. Observe agora a classe Círculo alterada:

class Circulo_1:
    _total_de_circulos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_de_circulos += 1

    @classmethod
    def get_total_de_circulos(cls):
        return cls._total_de_circulos

# Na linha 15, é criado o parâmetro cls como referência para classe. Na linha 16, é retornado o valor do atributo de classe _total_circulos.