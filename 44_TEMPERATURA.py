#Elabore um fluxograma e após crie um programa em python que converta temperaturas entre celsius e fahrenheit. O programa deve solicitar
#ao usuário que escolha o tipo de conversão que deseja realizar (celsius para fahrenheit ou fahrenheit para celsius). Após a escolha, leia 
#a temperatura e exiba o resultado da conversão.
#Celsius para fahrenheit: F = (C x 9/5) + 32
#Fahrenheit para celsius: C = (F - 32) x 5/

def converter_temperatura():
    print("Escolha o tipo de conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

    escolha = input("Digite 1 ou 2: ")

    if escolha == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} °C é igual a {fahrenheit} °F")
    
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} °F é igual a {celsius} °C")
    
    else:
        print("Opção inválida! Por favor, escolha 1 ou 2.")
if __name__ == "__main__":
    converter_temperatura()