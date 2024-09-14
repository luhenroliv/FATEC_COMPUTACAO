#10. Faça um algoritmo que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira nota e peso 3 para a segunda nota. (media ponderada = ((nota1 * 0.2) + (nota2 * 0,3))/2 
def calcular_media_ponderada(nota1, nota2, peso1=2, peso2=3):
    soma_dos_pesos = peso1 + peso2
    media_ponderada = ((nota1 * peso1) + (nota2 * peso2)) / soma_dos_pesos
    return media_ponderada

def main():
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
    except ValueError:
        print("Por favor, insira valores numéricos válidos para as notas.")
        return

    media = calcular_media_ponderada(nota1, nota2)

    print(f"A média ponderada das notas é {media:.2f}")

if __name__ == "__main__":
    main()
