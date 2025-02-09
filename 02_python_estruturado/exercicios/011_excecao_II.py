# Implementar uma solução que faça o tratamento de uma exceção de divisão por 0

while True:
    def divisao(num1, num2):
        try:
            resultado = num1/num2
            return f"\nO Quociente é >>> {resultado}\n"
                
        except ZeroDivisionError: # nativo do python
            return "\nO divisor não pode ser 0 !!!\n"

    num1 = int(input("\nDigite o n° dividendo >>> "))
    num2 = int(input("\nDigite o n° divisor >>> "))

    resposta = divisao(num1, num2)
    print(resposta)

    # para parar o programa após digitar os números certos e sair da exceção

    if "divisor não pode ser 0" not in resposta.lower():
        break