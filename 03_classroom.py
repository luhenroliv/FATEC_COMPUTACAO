##03- Estrutura_condicional
#comparação, atribuição, lógico
var = 5
print(var==5)
#TRUE
#comparação
#==
#!=
#>
#<
#>=
#<=
var = 5
var = var + 1
print(var)

var = True
print(not(var))
#false

#condição and
a = True
b = True
print(a and b)
#true

a = False
b = False
print(a and b)
#false

a = True
b = False
print(a and b)
#false

a = False
b = True
print(a and b)
#false

#condição OR

a = False
b = False
print(a and b)
#false

#Se houver um "V", o resultado retornará verdadeiro;

##

# Estrutura decisória simples
prova1 = 5
prova2 = 2.5
prova3 = 3
prova4 = 10
media = (prova1 + prova2 + prova3 + prova4) / 4

if media > 5:
    print("Aprovado")

# Estrutura decisória composta
#Exempo de aprovação inserindo nota;
prova1 = float(input("Digite a primeira nota"))
prova2 = float(input("Digite a segunda nota"))
prova3 = float(input("Digite a terceita nota"))
prova4 = float(input("Digite a quarta nota"))
media = (prova1 + prova2 + prova3 + prova4)/4
if media > 6:
    print("Aprovado")
elif media < 5:
    print("Reprovado")
else:
    print ("Recuperação")
    print(media)

    ##EXERCICIOS

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