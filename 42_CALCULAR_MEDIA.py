#Desenvolver um fluxograma e um programa em Python que leia o nome e as três notas obtidas por um aluno durante o semestre. Calcular a sua média (aritmética), informar o nome e sua menção aprovado (media >= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9).

def calcular_media():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        situacao = "Aprovado"
    elif media <= 5:
        situacao = "Reprovado"
    else:
        situacao = "Recuperação"
    print(f"\nNome: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
if __name__ == "__main__":
    calcular_media()