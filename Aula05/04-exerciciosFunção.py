#-----------------------------------------------------------------------------------------------------------------------------------------
#1. função para calcular a area do triangulo

def areaTiangulo ():
    base = float(input("Digite a base do triangulo: "))
    altura = float(input("Digite a altura do triangulo: "))
    area = (base * altura) / 2
    print(f" a rea do triangulo é: {area:.2f} ")

areaTiangulo()


def areaTiangulo (base,altura):
    area = (base * altura) / 2
    print(f" a rea do triangulo é: {area:.2f} ")

areaTiangulo(2,5)
#-----------------------------------------------------------------------------------------------------------------------------------------
#2. função para descobrir a area do quadrado
def areaQuadrado():
    lado = float(input("digite o tamanho do lado do quadrado: "))
    area = (lado**2)
    print(f"a area do quadrado é {area}")

areaQuadrado()

def areaQuadrado(lado):
    area = (lado**2)
    print(f"a area do quadrado é {area}")

areaQuadrado(2)

#-----------------------------------------------------------------------------------------------------------------------------------------
#3. Criar uma função que recebe um valor por parâmetro e informar se esse valor é par ou ímpar.

def parOuImpar ():
    num = int(input("Digite m número: "))
    if num % 2== 0:
        print(f"O numero {num} é par")
    else:
        print(f"O numero {num} é Ímpar")

parOuImpar()

def parOuImpar (num):
    if num % 2 == 0:
        print(f"O numero {num} é par")
    else:
        print(f"O numero {num} é Ímpar")

parOuImpar(7)


#-----------------------------------------------------------------------------------------------------------------------------------------

#Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def maior ():
    num1 = float(input("Digite o 1º número: "))
    num2 = float(input("Digite o 2º número: "))
    if num1 > num2:
        print(f" {num1} é maior que {num2}")
    else:
        print(f" {num2} é maior que {num1}")

maior()


def maior (num1, num2):
    if num1 > num2:
        print(f" {num1} é maior que {num2}")
    else:
        print(f" {num2} é maior que {num1}")

maior(5,10)
#-----------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------

#Escreva uma função que recebe um número n como parâmetro e imprime se n é positivo ou negativo.

def positivoOuNegativo():
    num = int(input("Informe um numero: "))
    if num > 0:
        print(f"O número {num} é positivo")
    else:
        print(f"O número {num} é negativo")

positivoOuNegativo()

#-----------------------------------------------------------------------------------------------------------------------------------------

