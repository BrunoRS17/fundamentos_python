"""Exercício4.2 Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h."""



velocidade_km = float(input("Digite a velocidade do carro: "))

if velocidade_km <= 80:
    print("Parábens, você não foi multado dessa vez.")

if velocidade_km > 80:
    #calcula multa somente se passou da velocidade
    valor_multa = (velocidade_km-80)*5
    print(f"Você foi multado, o valor é de R${valor_multa}")