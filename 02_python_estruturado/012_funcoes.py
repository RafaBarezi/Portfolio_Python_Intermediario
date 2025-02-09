def taximetro(distancia, mult=1):  # nome do subprograma e seus argumentos
    largada = 3
    km_rodado = 2
    valor = (largada+distancia*km_rodado) * mult
    return valor

pagamento = taximetro(3.5)
print("\n",pagamento, "\n")