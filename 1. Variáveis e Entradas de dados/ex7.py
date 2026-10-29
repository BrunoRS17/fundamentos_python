"""Escreva um programa que converta uma temperatura digitada em °C em °F."""


temperatura_C = float(input("Digite a temperatura em °C: "))

#Convertando para °F
temperatura_F = ((9*temperatura_C)/5) +32

#Monstrando o resultados
print(f"Temperatura em °C: {temperatura_C:.2f} °C")
print(f"Temperatura em °F: {temperatura_F:.2f} °F")
    