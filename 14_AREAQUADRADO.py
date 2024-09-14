#14. Faça um algoritmo que calcule e mostre a área de um quadrado. Sabe-se que: A = lado * lado; 
def calcular_area_quadrado(lado):
    return lado * lado

def main():
    try:
        lado = float(input("Digite o comprimento do lado do quadrado: "))
        if lado <= 0:
            print("O comprimento do lado deve ser maior que zero.")
            return
    except ValueError:
        print("Por favor, insira um valor numérico válido para o lado.")
        return

    area = calcular_area_quadrado(lado)

    print(f"A área do quadrado é {area:.2f}")

if __name__ == "__main__":
    main()