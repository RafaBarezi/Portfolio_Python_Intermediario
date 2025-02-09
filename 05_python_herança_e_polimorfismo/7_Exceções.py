class Excecao_Customizada(Exception):
    pass

def throws(): # throws gera uma instância da exceção
    raise Excecao_Customizada

# try e except servem para capturar a exceção gerada e imprimir uma mensagem indicando que a exceção foi criada:

try: # Essa é a tentativa, se der errado, será seguida a exceção
    throws()
except Excecao_Customizada as ex:
    print("\nExceção criada\n")

x = -1
if x < 0:
    raise Exception("Valor negativo!!!")

x = "hello"
if not type(x) is int:
    raise TypeError("Use apenas n°s inteiros")