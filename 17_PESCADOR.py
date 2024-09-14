#Toda vez que João “pescador” traz um peso de peixe maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 Quilos) deve pagar uma multa de R$4,00 por quilo excedente. João precisa que você faça um algoritmo que leia o peso de peixes e verifique se há excesso (mais que 50 Kg). Se houver, calcular e exibir o valor da multa (R$ 4,00 por cada Quilo acima de 50kg). Caso contrário mostrar a mensagem “sem excesso”. Ao final mostrar a mensagem “Verificação concluída”.
def calcular_multa(peso):
    limite_peso = 50
    valor_multa_por_kg = 4.00
    
    if peso > limite_peso:
        excesso = peso - limite_peso
        multa = excesso * valor_multa_por_kg
        return multa
    else:
        return 0.00

def main():
    try:
        peso = float(input("Digite o peso do peixe (em kg): "))
        
        if peso < 0:
            print("O peso não pode ser negativo.")
            return
        
        multa = calcular_multa(peso)
        
        if multa > 0:
            print(f"A multa é R${multa:.2f}.")
        else:
            print("Sem excesso.")
        
        print("Verificação concluída.")
    
    except ValueError:
        print("Por favor, insira um valor numérico válido para o peso.")

if __name__ == "__main__":
    main()
