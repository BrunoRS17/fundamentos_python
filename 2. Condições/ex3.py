"""Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a RS 1.250, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%."""

"""Neste momento no livro, ainda não tinha sido apresentado o 'else' ou o 'elif' """


#Solicitando os dados
salario = float(input("Qual o valor do seu salário? "))

#Calculando aumento com base no salário atual
if salario > 1_250:
    valor_aumento = salario * 0.10

if salario <= 1_250:
    valor_aumento = salario * 0.15


#Definindo o novo salário
novo_salario = valor_aumento + salario

#Exibindo resultados
print(f"Seu salário teve um aumento de R${valor_aumento:.2f}")
print(f"Salário Atual: {novo_salario:.2f}")


