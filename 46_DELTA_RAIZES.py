#Você é responsável por desenvolver uma solução para calcular as raizes de uma equação quadrática utilizando
#a formula de bhaskara. A formula de bhaskara é dada por:
#X = (-B ± raiz quadrada de Δ) / 2a, onde a, b e c são os coeficientes da equação quadrática:
#ax ao quadrado + bx + c = 0, e Δ = b ao quadrado - 4ac
#Se o discriminante Δ for negativo, a equação não possui raizes reais.
#Escreva o fluxograma, após desenvolva um programa python que leia os valores de "a,b,c" e, em seguida, calcule e exiba
#as raizes da equação, ou uma mensagem indicando que não existem raizes reais.

import math

def calcular_raizes():
    
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))
    
    
    delta = b**2 - 4 * a * c
    
    
    if delta < 0:
        print("Não existem raízes reais.")
    else:
        
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        
        
        print(f"As raízes da equação são: X1 = {x1:.2f} e X2 = {x2:.2f}")

if __name__ == "__main__":
    calcular_raizes()