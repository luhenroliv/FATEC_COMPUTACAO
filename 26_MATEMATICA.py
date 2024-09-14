#Desenvolva uma aplicação que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.
def main():
    try:
        a = int(input("Digite o valor A: "))
        b = int(input("Digite o valor B: "))
        
        if a == b:
            c = a + b
        else:
            c = a * b
        
        print(f"O valor de C é: {c}")
    
    except ValueError:
        print("Por favor, insira valores inteiros válidos.")

if __name__ == "__main__":
    main()