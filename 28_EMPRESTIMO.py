#A prefeitura de Jundiaí abriu uma linha de crédito para os funcionários estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. Desenvolva uma aplicação que permita entrar com o salário bruto e o valor da prestação, e informar se o empréstimo pode ou não ser concedido.
def main():
    try:
        salario_bruto = float(input("Digite o salário bruto: R$"))
        valor_prestacao = float(input("Digite o valor da prestação: R$"))
        
        limite_prestacao = salario_bruto * 0.30
        
        if valor_prestacao <= limite_prestacao:
            print("O empréstimo pode ser concedido.")
        else:
            print("O empréstimo não pode ser concedido.")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos para o salário bruto e o valor da prestação.")

if __name__ == "__main__":
    main()