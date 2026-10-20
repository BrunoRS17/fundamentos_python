"""Faça um programa que solicite o preço de uma mercadoria e o
percentual de desconto. Exiba o valor do desconto e o preço a pagar."""

preco_mercadoria = float(input("Insira o valor da mercadoria: "))
percentual_desconto = float(input("Insira o percentual de desconto: "))

valor_desconto = preco_mercadoria * (percentual_desconto/100)
preco_a_pagar = preco_mercadoria - valor_desconto

print(f"\nO valor de desconto é de R${valor_desconto:.2f}")
print(f"Valor a pagar é de R${preco_a_pagar:.2f}")