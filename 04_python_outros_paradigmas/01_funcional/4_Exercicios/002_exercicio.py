# Imprimir apenas números pares ou ímpares

lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ]

print(f"Listagem original = {lista}")

Test_par = lambda x: x % 2 == 0
Test_impar = lambda x: x % 2 != 0

pares = list(filter(Test_par, lista))
impares = list(filter(Test_impar, lista))

print("\n",f"Lista com apenas os números pares ={pares}")

print("\n",f"Lista com apenas os números ímpares ={impares}","\n")