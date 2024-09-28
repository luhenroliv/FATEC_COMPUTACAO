#Desenvolver um fluxograma e um programa em Python que, dada a idade de um nadador. Classifique-o em uma das seguintes categorias:
#Infantil A = 5 - 7 anos
#Infantil B = 8 - 10 anos
#Juvenil A = 11- 13 anos
#Juvenil B = 14 - 17 anos
#Sênior = 18 - 25 anos
#Apresentar mensagem “idade fora da faixa etária” quando for outro ano não contemplado.

def classificar_nadador():
    idade = int(input("Digite a idade do nadador: "))
    if 5 <= idade <= 7:
        categoria = "Infantil A"
    elif 8 <= idade <= 10:
        categoria = "Infantil B"
    elif 11 <= idade <= 13:
        categoria = "Juvenil A"
    elif 14 <= idade <= 17:
        categoria = "Juvenil B"
    elif 18 <= idade <= 25:
        categoria = "Sênior"
    else:
        categoria = "idade fora da faixa etária"
    print(f"Categoria: {categoria}")
if __name__ == "__main__":
    classificar_nadador()