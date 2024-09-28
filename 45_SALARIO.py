#Elabore um fluxograma e após desenvolva um programa em python que leia o salário atual de um funcionário e o percentual de aumento a ser aplicado. O programa deve calcular o novo salário e exibir o valor do aumento e o novo salário seguindo:
#- Se o salário for inferior a R$ 1.500,00, o aumento deve ser de 15%;
#- Se estiver entre R$ 1.500,00 e R$ 2.500,00, o aumento deve ser de 10%;
#- Se for superior a R$ 2.500,00, o aumento deve ser de 5%

def calcular_aumento_salario():
    salario = float(input("Digite o salário atual do funcionário: R$ "))
    
    if salario < 1500:
        aumento = salario * 0.15
    elif 1500 <= salario <= 2500:
        aumento = salario * 0.10
    else:
        aumento = salario * 0.05

    novo_salario = salario + aumento
    print(f"Aumento: R$ {aumento:.2f}")
    print(f"Novo Salário: R$ {novo_salario:.2f}")

if __name__ == "__main__":
    calcular_aumento_salario()