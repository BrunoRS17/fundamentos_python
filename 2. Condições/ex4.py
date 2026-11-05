"""Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e RS 0,45 para viagens mais longas."""


#Solicitiando distância em KM
distancia_km = int(input("Qual distância você irá percorrer (em km)? "))

#Definindo o valor do km com base na distância
if distancia_km <= 200:
    preco_por_km = 0.50
else:
    preco_por_km = 0.45

#Valor final
preco_passagem = distancia_km * preco_por_km

#Mostrando
print(f"total a pagar (R${preco_por_km:.2f}/km): R${preco_passagem:.2f}")


