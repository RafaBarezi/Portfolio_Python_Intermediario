class Conta:
    def __init__(self, titular, cpf, numero, saldo):
        self.titular = titular
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

def main():
    c1 = Conta("Joao", "123.456.789-10", "ag: 001 cc: 12345",
               "R$ 1000,00")  # Objeto sendo instanciado
    print(f"Nome do titular da conta: {c1.titular}")
    print(f"CPF do titular: {c1.cpf}")
    print(f"Número da conta: {c1.numero}")
    print(f"Saldo em caixa: {c1.saldo}", "\n")

    c2 = Conta("Maria", "123.456.789-11", "ag: 001 cc: 12346",
               "R$ 7600,00")  # Objeto sendo instanciado
    print(f"Nome do titular da conta: {c2.titular}")
    print(f"CPF do titular: {c2.cpf}")
    print(f"Número da conta: {c2.numero}")
    print(f"Saldo em caixa: {c2.saldo}", "\n")

    c3 = Conta("Joao", "123.456.789-12", "ag: 001 cc: 12347", "R$ 18000,00")
    print(f"Nome do titular da conta: {c3.titular}")
    print(f"CPF do titular: {c3.cpf}")
    print(f"Número da conta: {c3.numero}")
    print(f"Saldo em caixa: {c3.saldo}", "\n")

# Quando um script python é executado, a variável reservada  NAME referente a ele tem valor igual a "__main__".

# Nesse caso, a condição do IF a seguir será TRUE Então o que está no corpo do IF será executado. No caso, é um chamado ao método main do script:

if __name__ == "__main__":
    main()