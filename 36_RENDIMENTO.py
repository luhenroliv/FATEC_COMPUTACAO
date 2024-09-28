#Desenvolver um fluxograma e um programa em Python que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70%.

def calcular_rendimento():
    valor_depositado = float(input("Digite o valor depositado: R$ "))
    taxa_juro = 0.007  # 0,70%
    rendimento = valor_depositado * taxa_juro
    valor_total = valor_depositado + rendimento
    print(f"\nValor depositado: R$ {valor_depositado:.2f}")
    print(f"Rendimento após um mês: R$ {rendimento:.2f}")
    print(f"Valor total após um mês: R$ {valor_total:.2f}")
if __name__ == "__main__":
    calcular_rendimento()