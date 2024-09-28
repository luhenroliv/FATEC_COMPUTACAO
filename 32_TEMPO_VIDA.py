#Desenvolver um fluxograma e um programa em Python que receba o nome e a idade de uma pessoa. Calcule essa idade em meses, dias e horas. Mostre o nome e a idade em meses, dias e horas.

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade em anos: "))
idade_em_meses = idade * 12
idade_em_dias = idade * 365
idade_em_horas = idade_em_dias * 24
print(f"{nome}, sua idade em meses é: {idade_em_meses} meses")
print(f"{nome}, sua idade em dias é: {idade_em_dias} dias")
print(f"{nome}, sua idade em horas é: {idade_em_horas} horas")