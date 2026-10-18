"""Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos"""

#solicitando dados
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

#Transformando tudo em segundos
resultado_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

#exibe o resultado
print(f"{dias} dias, {horas}hrs, {minutos}min e {segundos}s é igual á {resultado_segundos}s")