#Faça um algoritmo que leia o Código e o Número de horas trabalhadas de um operário e calcule o salário base (chamado de SB) do mesmo, sabendo-se que ele ganha R$10,00 por hora. 
#Quando o número de horas trabalhadas for maior que 50, o trabalhador tem direito a um salário extra (chamado de SE). O salário extra consiste em R$ 20,00 por cada hora trabalhada acima das 50 horas iniciais. Calcule o salário extra (SE). Quando o trabalhador não tem direito ao salário extra, o valor do mesmo deve ser 0. 
#Ao final, calcular o salário total do trabalhador (chamado de ST) que consiste em: ST = SB + SE, mostrar o código do funcionário e o salário total (ST).
# Função para calcular o salário base e o salário extra
def calcular_salarios(numero_horas):
    valor_hora = 10.00
    salario_base = numero_horas * valor_hora
    
    if numero_horas > 50:
        horas_extras = numero_horas - 50
        salario_extra = horas_extras * 20.00
    else:
        salario_extra = 0.00

    salario_total = salario_base + salario_extra
    return salario_base, salario_extra, salario_total

def main():
    try:
        codigo = input("Digite o código do funcionário: ")
        numero_horas = float(input("Digite o número de horas trabalhadas: "))
        
        if numero_horas < 0:
            print("O número de horas trabalhadas não pode ser negativo.")
            return
        
        salario_base, salario_extra, salario_total = calcular_salarios(numero_horas)
        
        print(f"Código do funcionário: {codigo}")
        print(f"Salário Base (SB): R${salario_base:.2f}")
        print(f"Salário Extra (SE): R${salario_extra:.2f}")
        print(f"Salário Total (ST): R${salario_total:.2f}")
    
    except ValueError:
        print("Por favor, insira um valor numérico válido para as horas trabalhadas.")

if __name__ == "__main__":
    main()
