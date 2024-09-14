#Faça um algoritmo que leia um número e exiba caso este número seja menor que 10.
def main():
    try:
        numero = float(input("Digite um número: "))
        
        if numero < 10:
            print(f"O número digitado é: {numero}")
    
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == "__main__":
    main()