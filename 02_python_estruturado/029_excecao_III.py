try:
    num = eval(input("\nEntre com um número inteiro >>> "))
    print(f"\nVoce digitou {num}")
except ValueError:
    print("\nA função tem um argumento com o tipo correto, mas valor incorreto\n")
except IndexError:
    print("\nFora do intervalo de índices válidos\n")
except:
    print("\nOutro tipo de exceção\n")  # se eu digitar uma letra

# A instrução da linha 5 somente será executada se a exceção levantada no bloco try for do tipo ValueError e se, na instrução da linha 7, a exceção for do tipo IndexError.