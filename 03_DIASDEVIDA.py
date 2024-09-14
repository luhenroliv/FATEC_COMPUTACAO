#3. Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935 DIAS
def calcular_dias_de_vida(idade):
    dias_por_ano = 365
    return idade * dias_por_ano

def main():
    nome = input("Digite o seu nome: ")
    try:
        idade = int(input("Digite a sua idade: "))
        if idade < 0:
            print("A idade não pode ser negativa.")
            return
    except ValueError:
        print("Por favor, insira uma idade válida.")
        return

    dias_de_vida = calcular_dias_de_vida(idade)

    print(f"{nome.upper()}, VOCÊ JÁ VIVEU {dias_de_vida} DIAS")

if __name__ == "__main__":
    main()
