#Exibindo uma amostragem dos números de 0 a 100:
contador = 100
while contador >= 0:
    print(contador)
    contador -= 1

#Exibindo números impares de 0 a 100:
contador = 100
while contador >= 0:
    if contador % 2 != 0:  # Verifica se o número é ímpar
        print(contador)
    contador -= 1

#Exibindo números pares de 0 a 100:
contador = 100
while contador >= 0:
    if contador % 2 == 0:  # Verifica se o número é par
        print(contador)
    contador -= 1