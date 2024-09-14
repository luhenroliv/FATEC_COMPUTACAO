#11. Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%. (novo preço = preço antigo – (preço antigo *0,10)
def calcular_novo_preco(preco_antigo, desconto_percentual=10):
    desconto = preco_antigo * (desconto_percentual / 100)
    novo_preco = preco_antigo - desconto
    return novo_preco

def main():
    try:
        preco_antigo = float(input("Digite o preço do produto: "))
        if preco_antigo < 0:
            print("O preço não pode ser negativo.")
            return
    except ValueError:
        print("Por favor, insira um valor numérico válido para o preço.")
        return

    novo_preco = calcular_novo_preco(preco_antigo)

    print(f"O novo preço do produto após o desconto é R${novo_preco:.2f}")

if __name__ == "__main__":
    main()
