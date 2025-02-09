# Classes e objetos IV

import datetime


class Extrato:
    def __init__(self):
        self.transacoes = []

    def extrato(self, numeroconta):
        print(f"\nExtrato da conta conjunta: {numeroconta} \n")
        for p in self.transacoes:
            print(f"{p[0]} {p[1]} {p[2]} {p[3]}")