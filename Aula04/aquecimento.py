'''01- Peça para o usuário digitar dois nomes e imprima o maior deles utilizando F-STRING.'''

nome1 = input("1º nome: ")
nome2 = input("2º nome: ")

if len(nome1) > len(nome2):
    print(f"{nome1}")
elif len(nome2) > len(nome1)
    print(f"{nome2}")
else:
    print("Os dois nomes têm o mesmo tamanho")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''02- Solicite ao usuário um número inteiro e imprima na tela:
i) O quadrado do número caso seja par
ii) O cubo caso o número seja ímpar  '''

numero = int(input("Digite o número: "))

if (numero % 2 == 0):
    print(f"{numero ** 2}")
else:
    print(f"{numero ** 3}")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
''' 03 - Crie um programa que receba o valor de um capital investido, a taxa de juros, a modalidade (Simples ou Composto) 
e o tempo de aplicação e, ao final, mostre o montante.'''

capital = float(input("digite o capital investido:R$ "))
juros = float(input("digite o percentual da taxa de juros:"))
modalidade = int (input("Qual a modadalidade do juros? (1) SIMPLES ou (2) COMPOSTO "))
tempo = int(input("Qual o tempo da aplicação em meses? "))

taxa = juros / 100

if modalidade == 1:
    simples = capital * taxa * tempo
    montante = capital + simples
    print(f"O montante acumulado é de R${montante:.2f}")
elif modalidade == 2:
    composto = capital * ((1 + taxa) ** tempo)
    print(f"O montante acumulado é de R${composto:.2f}")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Solicite ao usuário que informe notas enquanto desejar e, ao final, informe a média das notas digitadas.'''

contador = 1
soma = 0
media = 1
while True:
    num = int(input(f'digite a {contador}ª nota: '))
    parar= input("Deseja continuar? SIM/NÃO")
    contador += 1
    soma = soma + num
    if parar == "sim":
        media += 1
        continue
    else:
        break
print(f" a media das notas é {soma/media:.2f}")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


