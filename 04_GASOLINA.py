#4. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque. (Litros = valor do pagamento / preço do litro)
def calcular_litros(preco_por_litro, valor_pagamento):
    if preco_por_litro <= 0:
        raise ValueError("O preço do litro deve ser maior que zero.")
    return valor_pagamento / preco_por_litro

def main():
    try:
        preco_por_litro = float(input("Digite o preço do litro da gasolina em reais: "))
        valor_pagamento = float(input("Digite o valor do pagamento em reais: "))
        
        if preco_por_litro <= 0 or valor_pagamento < 0:
            print("Os valores devem ser positivos e o preço do litro deve ser maior que zero.")
            return

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        return

    litros = calcular_litros(preco_por_litro, valor_pagamento)

    print(f"Você conseguiu colocar {litros:.2f} litros de gasolina no tanque.")

if __name__ == "__main__":
    main()
