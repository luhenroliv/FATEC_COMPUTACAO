#13. Faça um algoritmo que calcule e mostre a área de um trapézio. Sabe-se que: A = (base maior + base menor)* altura)/2 ;
def calcular_area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2

def main():
    try:
        base_maior = float(input("Digite o comprimento da base maior do trapézio: "))
        base_menor = float(input("Digite o comprimento da base menor do trapézio: "))
        altura = float(input("Digite a altura do trapézio: "))
        
        if base_maior <= 0 or base_menor <= 0 or altura <= 0:
            print("As dimensões devem ser maiores que zero.")
            return
    except ValueError:
        print("Por favor, insira valores numéricos válidos para as dimensões.")
        return

    area = calcular_area_trapezio(base_maior, base_menor, altura)

    print(f"A área do trapézio é {area:.2f}")

if __name__ == "__main__":
    main()