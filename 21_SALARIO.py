#Faça um algoritmo que leia 2 valores de salário e os exiba caso a média dos salários (Salário1 + Salário2 / 2) seja maior que R$2000,00. Ao final mostrar a mensagem “Fim do cálculo”.
def main():
    try:
        salario1 = float(input("Digite o primeiro salário: R$"))
        salario2 = float(input("Digite o segundo salário: R$"))
        
        media_salarios = (salario1 + salario2) / 2
        
        if media_salarios > 2000:
            print(f"Salário 1: R${salario1:.2f}")
            print(f"Salário 2: R${salario2:.2f}")
        
        print("Fim do cálculo.")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos para os salários.")

if __name__ == "__main__":
    main()