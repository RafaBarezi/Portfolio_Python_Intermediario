# Para controlar a quantidade de círculos criados:

class Circulo(): # Classe Círculo com atributo de classe
    _total_circulos = 0 # Como a declaração está localizada antes do init, o interpretador “entende” que se trata de uma variável de classe, ou seja, que terá um valor único para todos objetos da classe.

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        self._total_circulos += 1