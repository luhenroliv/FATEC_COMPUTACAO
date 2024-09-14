#5. O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.
def calcular_valor_a_pagar(peso_prato, preco_por_quilo=12.00):
    return peso_prato * preco_por_quilo

def main():

    try:
        peso_prato = float(input("Digite o peso do prato montado (em quilos): "))
        
        if peso_prato < 0:
            print("O peso do prato não pode ser negativo.")
            return

    except ValueError:
        print("Por favor, insira um valor numérico válido para o peso.")
        return

    valor_a_pagar = calcular_valor_a_pagar(peso_prato)

    print(f"O valor a pagar é R${valor_a_pagar:.2f}")

if __name__ == "__main__":
    main()
