#FATEC
#EXERCICES:

#Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935 DIAS.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
dias = int(idade) * 365
print(f"{nome} você já viveu {dias} dias")


#Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque. (Litros = valor do pagamento / preço do litro).
preco_litro = float(input("Digite o preço do litro da gasolina: "))
pagamento = float(input("Digite o valor do pagamento: "))
litros = pagamento / preco_litro
#print("Você colocou %.2f litros" %(litros))
print(f"Você colocou {litros:.2f} litros")
#print(f"Porcentagem: {litros:.2%}")

#O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.
peso = float(input("Digite o valor do peso em KG: "))
prato = 0.2
valor = (peso-prato) * 12
valor = valor.replace('.',',')
print(f"O valor a pagar é R${valor}")