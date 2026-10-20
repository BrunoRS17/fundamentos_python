"""Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem."""

#Adquiri os dados
distancia_km = float(input("Insira a distância (km): "))
velocidade_media = float(input("Insira a velocidade média (km/h): "))

#Calcula o tempo
tempo = distancia_km/velocidade_media

#Transforma o tempo de decimais para sexagesimal
horas = int(tempo)
minutos = (tempo - horas) * 60
segundos =  (minutos - int(minutos)) * 60

#Mostra o resultados
print(f"Percorrendo {distancia_km:.2f}km á uma velocidaade média de {velocidade_media:.2f}km/h, você chegará ao destino em {horas} horas, {int(minutos)} minutos e {int(segundos)}s")