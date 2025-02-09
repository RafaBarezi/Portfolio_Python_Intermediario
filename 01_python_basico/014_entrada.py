# Entradas

nome = input("\nDigite seu nome >>> ")
print("Seu nome é", nome,"\n")

numero = eval(input("Digite um número >>> "))
# O sistema armazena como string, para reconhecer como valor, é preciso usar o eval()
numero = numero + 10
print("numero digitado mais 10 é igual a", numero, "\n")

"""

Exemplo: calculo IMC

peso = eval(input("por favor , digite seu peso:"))
altura = eval(input("por favor, digite sua altura:"))
imc = peso/(altura **2)
print("imc", imc)

"""