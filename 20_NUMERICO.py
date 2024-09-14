#Faça um algoritmo que leia dois números e os exiba na tela somente se o valor da soma desses dois números for maior que 20. Caso contrário, não mostrar nada.
def main():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        soma = numero1 + numero2
        
        if soma > 20:
            print(f"Os números digitados são: {numero1} e {numero2}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
