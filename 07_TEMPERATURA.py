#7. Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit. Faça um algoritmo para ler uma temperatura Celsius e imprimi-Ia em Fahrenheit (pesquise como fazer este tipo de conversão).
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():

    try:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
    except ValueError:
        print("Por favor, insira um valor numérico válido.")
        return

    fahrenheit = celsius_para_fahrenheit(celsius)

    print(f"A temperatura em graus Fahrenheit é {fahrenheit:.2f}")

if __name__ == "__main__":
    main()