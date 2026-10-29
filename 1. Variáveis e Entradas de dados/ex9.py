"""Exercício 3.15 Escreva um programa para calcular a redução do tempo de vidade um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

#Adquirindo as informações
quantidade_cigarros_dias=int(input("Quantos cigarros você fuma em média por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))

#Calculando tempo de vida perdido
quantidade_de_dias_fumando = anos_fumando*365

tempo_perdido_minutos = (quantidade_cigarros_dias*quantidade_de_dias_fumando)*10
tempo_perdido_dias = tempo_perdido_minutos/1440
tempo_perdido_anos = tempo_perdido_dias/365

#Exibindo resultado
print(f"Você já perdeu {tempo_perdido_dias:.2f} dias por fumar, o que é, aproximadamente {tempo_perdido_anos:.2f} anos")

