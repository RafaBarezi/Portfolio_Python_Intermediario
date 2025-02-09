# Tratamento de exceção com looping, para que não encerre após a primeira verificação

while True:
    try:
        num = int(input("\nEntre com um número inteiro: \n"))
        print(f"\nO número digitado foi {num}\n")
        break # O break vai interromper quando o usuário digitar o valor certo.

    except ValueError: # nativo do python 
        print("\nEntre com o valor numérico e não letras\n")