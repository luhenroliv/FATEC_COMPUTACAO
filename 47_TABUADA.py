#Vamos usar a estrutura while para criar um programa que gera a tabuada
#de qualquer número.
#Esse exercício permitirá entender como a repetição é usada para automatizar tarefas, como
#calcular a multiplicação repetidamente.

numero = int(input("Digite um número para ver sua tabuada: "))
#Inicializa o contador
contador = 1
#Usa a estrutura while para gerar a tabuada
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1