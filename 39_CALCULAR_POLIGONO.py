#Desenvolver um fluxograma e um programa em Python que leia o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte:
#Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área;
#Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área;
#Se o número de lados for igual a 5 escrever PENTÁGONO;
#Se número de lados for inferior a 3 escrever NÃO É UM POLÍGONO;
#Se número de lados for superior a 5 escrever POLÍGONO NÃO IDENTIFICADO;

import math
def calcular_poligono():
    num_lados = int(input("Digite o número de lados do polígono: "))
    medida_lado = float(input("Digite a medida do lado (em cm): "))
    if num_lados < 3:
        print("NÃO É UM POLÍGONO")
    elif num_lados == 3:
        area = (math.sqrt(3) / 4) * (medida_lado ** 2) 
        print(f"TRIÂNGULO\nÁrea: {area:.2f} cm²")
    elif num_lados == 4:
        area = medida_lado ** 2  
        print(f"QUADRADO\nÁrea: {area:.2f} cm²")
    elif num_lados == 5:
        print("PENTÁGONO")
    else:
        print("POLÍGONO NÃO IDENTIFICADO")
if __name__ == "__main__":
    calcular_poligono()