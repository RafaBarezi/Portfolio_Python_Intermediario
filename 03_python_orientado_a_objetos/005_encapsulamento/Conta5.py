class Conta5:

    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo


def main():
    conta = Conta5("001", 1000)
    saldo = conta.saldo
    print(conta.__saldo)


if __name__ == "__main__":
    main()

# Para tornar um atributo privado, é preciso iniciá-lo com dois underscores (‘__’). Um erro será gerado porque o atributi não está disponível.