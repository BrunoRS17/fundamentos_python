"""Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias
pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado."""


#Adquirindo os dados
quantidade_km = float(input("Qual a quantidade de Km rodados? "))
quantidade_dias = int(input("Por quantos dias o carro foi alugado? "))

#Calculando preço
valor_dia = 60*quantidade_dias
valor_km = 0.15 * quantidade_km
valor_total = valor_dia + valor_km

#Exibindo resultados
print(f"Valor final: R${valor_total:.2f}")
print(f"Valor total por dia: R${valor_dia:.2f}")
print(f"Valor por km: R${valor_km:.2f}")