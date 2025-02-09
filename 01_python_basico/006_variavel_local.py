# Variável local

def multiplicador(numero):
    a = 2  # esta variável tem escopo local
    print(f"\nDentro da função, a variável vale: {a}")
    return a * numero

a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"\nFora da função, a variável a vale: {a}")

# Quando o python não encontra nada na variável local ele procura no escopo global

def multiplicador(numero):
    return c * numero

c = 3  # esta variável tem escopo global
d = multiplicador(5)
print(f"\nA variável d vale: {d}\n")

# A ordem utilizada para a procura do escopo é: Função delimitadora / Variáveis globais / módulo builtins