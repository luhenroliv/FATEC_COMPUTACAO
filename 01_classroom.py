#01.FISRT EXAMPLE:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
days_of_life = age * 365
print(f"{name.upper()}, you have already lived {days_of_life} days.");

#02.INTRODUCTION:
print("Hello world!")

#03.VARIABLES AND CONCATENATION
n_integer = 10
n_float = 10.75
n_string = "10"
n_boolean = True

age = 30
name = "Luis"
type(age)

print("Hello "+name+", you are "+str(age)+" years old")

#04.VARIABLES TO ARGUMENTS
age = 30
name = "Luis"
print("Hello",name,", you are",age,"years old.")

#05.FORMATTED VARIABLES AND STRINGS
age = 30
name = "Luis"
print(f"Hello {name}, you are {age} years old")
print("Hello {}, you are {} years old".format(name, age))

#06.VARIABLES AND OLD FORMATTING
age = 30
name = "Luis"
salary = 50.25432456444532
print("Hello %s , you are %d years old and your salary is %.2f" %(name, age, salary))

#07.INPUT
age = input("Enter your age: ")
name = input("Enter your name: ")
print(f"Hello {name}, you are {age} years old")

#08.ARITHMETIC OPERATORS
soma = 10 + 5
sub = 10 - 5
div = 10 / 5
mult = 10 * 5
resto = 9 % 2
exp = 3 ** 2
raiz = 9 ** 0.5 # ou 9 ** (1/2)
div_integer = 9 // 2
print(div_integer)

#09.EXERCICES:

A imobiliária Imóbilis vende apenas terrenos retangulares. Faça um algoritmo para ler as dimensões de um terreno e depois exibir a área do terreno.

comprimento = input("Digite o comprimento do terreno: ")
largura = input("Digite a largura do terreno: ")
area = float(comprimento) * float(largura)
print(f"O terreno tem {area} metros quadrados")


Faça um algoritmo para calcular quantas ferraduras são necessárias para equipar todos os cavalos comprados para um haras.
qtd_cavalos = input("Digite a quantidade de cavalos do haras: ")
qtd_ferraduras = int(qtd_cavalos) * 4
print(f"O haras necessita de {qtd_ferraduras} ferraduras")