#Desenvolver um fluxograma e um programa em Python para ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é: F= 9*C/ 5 +32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius. Ao final exibir as duas temperaturas.

def converter_temperatura():
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = (9 * celsius / 5) + 32
    print(f"\nTemperatura em Celsius: {celsius:.2f} °C")
    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
if __name__ == "__main__":
    converter_temperatura()