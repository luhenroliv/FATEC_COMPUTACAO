#Faça um algoritmo que leia 2 números e os exiba em ordem decrescente (primeiro o maior, depois o menor).
def main():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        if numero1 > numero2:
            print(f"Ordem decrescente: {numero1}, {numero2}")
        else:
            print(f"Ordem decrescente: {numero2}, {numero1}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
