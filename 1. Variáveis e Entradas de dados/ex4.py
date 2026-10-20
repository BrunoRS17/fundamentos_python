"""Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor
do aumento e do novo salário.
"""

#Aquiri os dados
salario_atual = float(input("Qual o valor do seu salário atual? "))
porcentagem_aumento = float(input("Qual a porcentagem de aumento? "))

#Realiza o calculo
salario_com_aumento = salario_atual + (salario_atual * (porcentagem_aumento/100))

#Mostra o resultadp
print(f"Seu salário com um aumento de {porcentagem_aumento:.2f}% foi para R${salario_com_aumento:.2f}")
