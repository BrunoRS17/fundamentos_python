"""Exercício 4.8 Reescreva o Programa 4.4 e calcule a conta da operadora Tchau usando else"""

#Solicita o plano
plano = input("Qual o seu plano? ")

#Define valores para o plano
if plano == "falamuito" or plano == "falapouco":

    if plano == "falapouco":
        minutos_plano = 100
        preco_minutos_extras = 0.20
        preco_plano = 50


    if plano == "falamuito":
        minutos_plano = 500
        preco_minutos_extras = 0.15
        preco_plano = 99


    #Calcula valor a pagar e mostra com base no total de minutos consumidos
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))

    print("Preço a pagar:")
    print(f"valor do plano: R${preco_plano:.2f}")

    suplemento = 0 #Defini valores de minutos excendente 

    if minutos_consumidos > minutos_plano:
        suplemento = preco_minutos_extras * (minutos_consumidos-minutos_plano)
        print(f"preço de suplemento ({(minutos_consumidos - minutos_plano):.2f} min): R${suplemento:.2f}")

    print(f"\nTotal a pagar: R${(suplemento + preco_plano):.2f}")


#Plano desconhecido
else:
    print("Não conheço este plano")



    





