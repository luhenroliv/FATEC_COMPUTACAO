#1. A imobiliária Imóbilis vende apenas terrenos retangulares. Faça um algoritmo para ler as dimensões de um terreno e depois exibir a área do terreno.
# Função para calcular a área do terreno
def calcular_area(largura, comprimento):
    return largura * comprimento

def main():
    largura = float(input("Digite a largura do terreno em metros: "))
    comprimento = float(input("Digite o comprimento do terreno em metros: "))

    area = calcular_area(largura, comprimento)

    print(f"A área do terreno é {area} metros quadrados.")

if __name__ == "__main__":
    main()
