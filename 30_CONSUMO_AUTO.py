#Desenvolver um fluxograma e um programa em Python para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto. CONSUMO=DITANCIA_PERCORRIDA/COMBUSTIVEL_GASTO.

distancia_percorrida = float(input("Digite a distância total percorrida (em km): "))
combustivel_gasto = float(input("Digite o total de combustível gasto (em litros): "))
consumo_medio = distancia_percorrida / combustivel_gasto
print("O consumo médio do automóvel é:", consumo_medio, "km/l")