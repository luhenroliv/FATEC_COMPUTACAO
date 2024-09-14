#Toda vez que João “pescador” traz um peso de peixe maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50
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
            print(f"O peso do peixe excedeu o limite. A multa é R${multa:.2f}.")
        else:
            print("O peso do peixe está dentro do limite. Não há multa.")
    
    except ValueError:
        print("Por favor, insira um valor numérico válido para o peso.")

if __name__ == "__main__":
    main()
