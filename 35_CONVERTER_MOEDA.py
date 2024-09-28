#Desenvolver um fluxograma e um programa em Python que efetue a apresentação do valor da conversão das moedas em dólar, euro e libra de um valor lido em real. O algoritmo deverá solicitar a quantidade de reais disponíveis, o valor de cada moeda e fazer as referidas cotações.

def converter_moedas():
    reais = float(input("Digite a quantidade de reais disponíveis: R$ "))
    valor_dolar = float(input("Digite o valor do dólar: R$ "))
    valor_euro = float(input("Digite o valor do euro: R$ "))
    valor_libra = float(input("Digite o valor da libra: R$ "))
    dolares = reais / valor_dolar
    euros = reais / valor_euro
    libras = reais / valor_libra
    print(f"\nCom R$ {reais:.2f} você pode comprar:")
    print(f"{dolares:.2f} dólares")
    print(f"{euros:.2f} euros")
    print(f"{libras:.2f} libras")
if __name__ == "__main__":
    converter_moedas()