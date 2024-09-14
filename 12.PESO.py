#12. Faça um algoritmo que receba o peso de uma pessoa em quilos, calcule e mostre esse peso em gramas. (sabe-se que 1kg equivale a 1000 g)
def converter_quilos_para_gramas(peso_quilos):
    return peso_quilos * 1000

def main():
    try:
        peso_quilos = float(input("Digite o peso da pessoa em quilos: "))
        if peso_quilos < 0:
            print("O peso não pode ser negativo.")
            return
    except ValueError:
        print("Por favor, insira um valor numérico válido para o peso.")
        return

    peso_gramas = converter_quilos_para_gramas(peso_quilos)

    print(f"O peso em gramas é {peso_gramas:.0f}")

if __name__ == "__main__":
    main()
