#Desenvolva uma aplicação que receba um valor inteiro e exiba se ele é par, ímpar ou zero.
def main():
    try:
        valor = int(input("Digite um valor inteiro: "))
        
        if valor == 0:
            print("O valor é zero.")
        elif valor % 2 == 0:
            print("O valor é par.")
        else:
            print("O valor é ímpar.")
    
    except ValueError:
        print("Por favor, insira um valor inteiro válido.")

if __name__ == "__main__":
    main()
