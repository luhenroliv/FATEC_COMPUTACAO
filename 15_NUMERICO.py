#Faça um algoritmo para ler um número e exibi-lo somente se o mesmo for maior que 100. Caso contrário exiba o valor 0 (zero).
def main():
    try:
        numero = float(input("Digite um número: "))
        
        if numero > 100:
            print(f"O número digitado é: {numero}")
        else:
            print("O valor é 0")
    
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == "__main__":
    main()
