#2. Faça um algoritmo para calcular quantas ferraduras são necessárias para equipar todos os cavalos comprados para um haras.
def calcular_ferraduras(numero_de_cavalos):
    ferraduras_por_cavalo = 4
    return numero_de_cavalos * ferraduras_por_cavalo

def main():

    try:
        numero_de_cavalos = int(input("Digite o número de cavalos: "))
        if numero_de_cavalos < 0:
            print("O número de cavalos não pode ser negativo.")
            return
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        return

    total_ferraduras = calcular_ferraduras(numero_de_cavalos)

    print(f"Para equipar {numero_de_cavalos} cavalos, são necessárias {total_ferraduras} ferraduras.")

if __name__ == "__main__":
    main()
