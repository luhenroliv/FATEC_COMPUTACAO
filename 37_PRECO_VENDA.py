#Desenvolver um fluxograma e um programa em Python que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

def calcular_preco_venda():
    preco_custo = float(input("Digite o preço de custo do produto: R$ "))
    percentual_acrescimo = float(input("Digite o percentual de acréscimo: "))
    valor_venda = preco_custo + (preco_custo * percentual_acrescimo / 100)
    print(f"\nPreço de custo: R$ {preco_custo:.2f}")
    print(f"Percentual de acréscimo: {percentual_acrescimo:.2f}%")
    print(f"Valor de venda: R$ {valor_venda:.2f}")
if __name__ == "__main__":
    calcular_preco_venda()