# Calcular o valor de compra:

# Preço unitario R$ 10.00 //
# Compras até 10 unidades não tem desconto
# compras de 11 a 20 unidades tem desconto de 10%
# compras acima de 20 unidades tem desconto de 20%

quant = eval(input("\nPor favor, digite quantos produtos deseja >>> "))

custo_final = 10.00 * quant

if (quant <= 10):
    print(f"\nValor final da compra: {custo_final}\n")
elif (quant <= 20):
    print(f"\nValor do desconto recebido: R${custo_final * 0.1}")
    print(
        f"\nValor final da compra(Já com desconto): {custo_final-(custo_final * 0.1)},\n")
else:
    print(f"\nValor do desconto recebido: R${custo_final * 0.2}")
    print(
        f"\nValor final da compra(Já com desconto): {custo_final-(custo_final * 0.2)}\n")