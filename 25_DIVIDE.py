#Desenvolva uma aplicação para determinar se um número A é divisível por um outro número B. Esses valores devem ser fornecidos pelo usuário.
def main():
    try:
        a = int(input("Digite o número A: "))
        b = int(input("Digite o número B: "))
        
        if b == 0:
            print("O número B não pode ser zero, pois divisão por zero não é permitida.")
        elif a % b == 0:
            print(f"O número {a} é divisível por {b}.")
        else:
            print(f"O número {a} não é divisível por {b}.")
    
    except ValueError:
        print("Por favor, insira valores numéricos inteiros válidos.")

if __name__ == "__main__":
    main()
