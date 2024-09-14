#8. Faça um algoritmo que receba três números, calcule e mostre a multiplicação desses números.
def multiplicar_tres_numeros(numero1, numero2, numero3):
    return numero1 * numero2 * numero3

def main():

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        numero3 = float(input("Digite o terceiro número: "))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        return

    resultado = multiplicar_tres_numeros(numero1, numero2, numero3)

    print(f"A multiplicação dos números é {resultado:.2f}")

if __name__ == "__main__":
    main()
