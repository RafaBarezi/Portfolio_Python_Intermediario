# Tratamento de exceção: (Para não permitir vulnerabilidade)

try:
    num = eval(input("\nEntre com um número inteiro: \n"))
    print(f"\nO número digitado foi {num}\n")
except:
    print("\nEntre com o valor numérico e não letras\n")