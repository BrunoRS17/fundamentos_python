"""Exercício 4.3 Escreva um programa que leia três números e que imprima o maior e o menor"""

"""Neste momento no livro, ainda não tinha sido apresentado o 'else' ou o 'elif' """

#Adquirindo os números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))


#Verifica quais os maiores e os menores
if numero1 > numero2 and numero1 > numero3:
    print("O primeiro número é o maior")
    if numero2 > numero3:
        print("O terceiro número é o menor")
    if numero3 > numero2:
        print("O segundo número é o menor")


if numero2 > numero1 and numero2 > numero3:
    print("O segundo número é o maior")
    if numero1 > numero3:
        print("O terceiro número é o menor")
    if numero3 > numero1:
        print("O primeiro número é o menor")


if numero3 > numero1 and numero3 > numero2:
    print("O terceiro número é o maior")
    if numero2 > numero1:
        print("O primeiro número é o menor")
    if numero1 > numero2:
        print("O segundo número é o menor")
