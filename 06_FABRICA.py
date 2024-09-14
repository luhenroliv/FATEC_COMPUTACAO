#6. Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado.
def calcular_valor_arrecadado(qtd_pequenas, qtd_medianas, qtd_grandes):
    preco_pequena = 10.00
    preco_mediu = 12.00
    preco_grande = 15.00
    return (qtd_pequenas * preco_pequena +
            qtd_medianas * preco_mediu +
            qtd_grandes * preco_grande)

def main():

    try:
        qtd_pequenas = int(input("Digite a quantidade de camisetas pequenas: "))
        qtd_medianas = int(input("Digite a quantidade de camisetas médias: "))
        qtd_grandes = int(input("Digite a quantidade de camisetas grandes: "))
        
        if qtd_pequenas < 0 or qtd_medianas < 0 or qtd_grandes < 0:
            print("As quantidades não podem ser negativas.")
            return

    except ValueError:
        print("Por favor, insira valores inteiros válidos para as quantidades.")
        return

    valor_arrecadado = calcular_valor_arrecadado(qtd_pequenas, qtd_medianas, qtd_grandes)

    print(f"O valor arrecadado será R${valor_arrecadado:.2f}")

if __name__ == "__main__":
    main()
