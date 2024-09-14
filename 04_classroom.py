#Toda vez que João “pescador” traz um peso de peixe maior que o estabelecido pelo 
# regulamento de pesca do estado de São Paulo (50 Quilos) 
# deve pagar uma multa de R$4,00 por quilo excedente. 
# João precisa que você faça um algoritmo que leia o peso de peixes
# e verifique se há excesso (mais que 50 Kg). Se houver,
# calcular e exibir o valor da multa (R$ 4,00 por cada Quilo acima de 50kg).
# Caso contrário mostrar a mensagem “sem excesso”. Ao final mostrar a mensagem “Verificação concluída”.

#Exercicio3
def verificar_peso_peixes(peso_peixes):
    limite_peso = 50
    valor_multa_por_quilo = 4.00

    if peso_peixes > limite_peso:
        excesso = peso_peixes - limite_peso
        multa = excesso * valor_multa_por_quilo
        print(f"Excesso de peso: {excesso:.2f} kg")
        print(f"Valor da multa: R$ {multa:.2f}")
    else:
        print("Sem excesso")

    print("Verificação concluída")

peso_peixes = float(input("Digite o peso dos peixes em Kg: "))
verificar_peso_peixes(peso_peixes)