#Desenvolver um fluxograma e um programa em Python que leia a altura e peso de uma pessoa e calcule o IMC. O índice de massa corpórea (IMC) pode ser obtido pela fórmula: peso / (altura2).
#imc < 18.5, escrever “MAGRO”,
#imc >= 18.5 e imc < 25, escrever “NORMA!”
#imc >= 25 e imc < 30, escrever "SOBREPESO”
#imc >=30 e imc < 40, escrever “OBESO!”
#imc >= 30, escrever "OBESO MORBIDO

def calcular_imc():
    altura = float(input("Digite a altura em metros: "))
    peso = float(input("Digite o peso em kg: "))
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "MAGRO"
    elif 18.5 <= imc < 25:
        classificacao = "NORMA!"
    elif 25 <= imc < 30:
        classificacao = "SOBREPESO"
    elif 30 <= imc < 40:
        classificacao = "OBESO!"
    else:
        classificacao = "OBESO MÓRBIDO"
    print(f"IMC: {imc:.2f} - Classificação: {classificacao}")
if __name__ == "__main__":
    calcular_imc()