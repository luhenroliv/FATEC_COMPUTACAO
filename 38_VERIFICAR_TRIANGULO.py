#Desenvolver um fluxograma e um programa em Python que leia 3 valores A, B, C e exiba se é um triângulo Isóscele, equilátero, escaleno ou se não é triângulo. 
#• É triângulo quando cada um dos lados for menor que a soma dos outros dois;
#• É triângulo Equilátero quando todos os lados forem iguais;
#• É triângulo Escaleno quando todos os lados forem diferentes;
#• É triângulo Isósceles quando dois lados forem iguais e um diferente.

def verificar_triangulo():
    A = float(input("Digite o valor do lado A: "))
    B = float(input("Digite o valor do lado B: "))
    C = float(input("Digite o valor do lado C: "))
    if A < B + C and B < A + C and C < A + B:
        if A == B == C:
            tipo = "Equilátero"
        elif A == B or B == C or A == C:
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"
        print(f"Os lados formam um triângulo {tipo}.")
    else:
        print("Os lados não formam um triângulo.")
if __name__ == "__main__":
    verificar_triangulo()