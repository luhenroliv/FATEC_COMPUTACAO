#Desenvolva uma aplicação que receba dois valores numéricos inteiros, calcule e mostre o resultado da diferença do maior pelo menor valor.
def main():
    try:
        valor1 = int(input("Digite o primeiro valor inteiro: "))
        valor2 = int(input("Digite o segundo valor inteiro: "))
        
        maior_valor = max(valor1, valor2)
        menor_valor = min(valor1, valor2)
        
        diferença = maior_valor - menor_valor
        
        print(f"A diferença entre o maior e o menor valor é: {diferença}")
    
    except ValueError:
        print("Por favor, insira valores inteiros válidos.")

if __name__ == "__main__":
    main()
