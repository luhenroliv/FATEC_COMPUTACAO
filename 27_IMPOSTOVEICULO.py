#Num determinado Estado, para transferências de veículos, o DETRAN cobra uma taxa de 1% para carros fabricados antes de 1990 e uma taxa de 1.5% para os fabricados de 1990 em diante. A taxa é aplicada diretamente sobre o preço do carro. Desenvolva uma aplicação que leia o ano e o preço do carro e a seguir calcule e imprime o imposto a ser pago.
def main():
    try:
        ano_fabricacao = int(input("Digite o ano de fabricação do carro: "))
        preco_carro = float(input("Digite o preço do carro: R$"))
        
        if ano_fabricacao < 1990:
            taxa_imposto = 0.01  # 1%
        else:
            taxa_imposto = 0.015  # 1.5%
        
        imposto = preco_carro * taxa_imposto
        
        print(f"O imposto a ser pago é: R${imposto:.2f}")
    
    except ValueError:
        print("Por favor, insira valores válidos para o ano e o preço do carro.")

if __name__ == "__main__":
    main()