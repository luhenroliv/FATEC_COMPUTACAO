#Desenvolva uma aplicação que receba um valor inteiro e exiba se ele é divisível por X, onde X é a soma dos dígitos do seu RM.
def soma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

def main():
    try:
        valor = int(input("Digite um valor inteiro: "))
        rm = input("Digite o RM (Registro de Matrícula): ")
        
        soma_dos_digitos_rm = soma_digitos(rm)
        
        if soma_dos_digitos_rm == 0:
            print("A soma dos dígitos do RM é 0. Divisão por zero não é permitida.")
        elif valor % soma_dos_digitos_rm == 0:
            print(f"O valor {valor} é divisível pela soma dos dígitos do RM ({soma_dos_digitos_rm}).")
        else:
            print(f"O valor {valor} não é divisível pela soma dos dígitos do RM ({soma_dos_digitos_rm}).")
    
    except ValueError:
        print("Por favor, insira um valor inteiro válido para o valor e um RM válido para o Registro de Matrícula.")

if __name__ == "__main__":
    main()
