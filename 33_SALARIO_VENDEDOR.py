#Desenvolver um fluxograma e um programa em Python que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo, o valor da comissão e salário no final do mês.

def calcular_salario_vendedor():
    nome = input("Digite o nome do vendedor: ")
    salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
    total_vendas = float(input("Digite o total de vendas efetuadas: R$ "))
    comissao = total_vendas * 0.15
    salario_total = salario_fixo + comissão
    print("\n--- Resultados ---")
    print(f"Nome do vendedor: {nome}")
    print(f"Salário fixo: R$ {salario_fixo:.2f}")
    print(f"Valor da comissão: R$ {comissao:.2f}")
    print(f"Salário total no final do mês: R$ {salario_total:.2f}")
if __name__ == "__main__":
    calcular_salario_vendedor()