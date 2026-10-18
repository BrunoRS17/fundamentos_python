"""Escreva um programa que leia um valor em metros e o exiba convertido em milímetros."""

#Solicita o valor em mêtros
valor_metros = float(input("Digite um valor em mêtros: "))

#Conversão
valor_milimetros = valor_metros*1000

#exibe resultado
print(f"\nO valor {valor_metros}m convertido para milímetros é: {valor_milimetros:.2f}mm")