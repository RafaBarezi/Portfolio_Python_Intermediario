# Atribuição multipla

a, b = 1, 2
print("\nAntes da troca:")
print(f"O valor das variáveis>>> a = {a}, b = {b}","\n")

#Primeira troca

temp = a    
a = b 
b = temp
print("Primeira troca:")
print(f"O valor das variáveis>>> a = {a}, b = {b}","\n")

#Segunda troca

a, b = b, a
print("Segunda troca:")
print(f"O valor das variáveis>>> a = {a}, b = {b}","\n")