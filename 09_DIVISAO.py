#9. Faça um algoritmo que receba dois números, calcule e mostre a divisão do primeiro número pelo segundo. Sabe-se que o segundo número não pode ser zero, portanto não é necessário se preocupar com validações.
def dividir_numeros(numero1, numero2):
    return numero1 / numero2

def main():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        return

    resultado = dividir_numeros(numero1, numero2)

    print(f"A divisão de {numero1} por {numero2} é {resultado:.2f}")

if __name__ == "__main__":
    main()
