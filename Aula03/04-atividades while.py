# Imprima em tela a sequência de 0 até 50.

contador = 0
while contador <= 50:
    print(contador)
    contador +=1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Imprima em tela a sequência de 100 até 0.

contador = 100
while contador >= 0:
    print(contador)
    contador -=1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Imprima em tela a sequência de 50 até 10.

contador = 50
while contador >= 10:
    print(contador)
    contador -=1    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Imprima em tela a sequência de 70 até 94.

contador = 70
while contador <= 94:
    print(contador)
    contador +=1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Imprima todos os números pares de 0 à 100.
# Logo depois, imprima todos os números ímpares de 0 à 100.

contador = 0
while contador <= 100:
    if contador % 2 == 0:
        print(contador)
    contador += 1

contador1 = 0
while contador1 <= 100:
    if contador1 % 2 != 0:
        print(contador1)
    contador1 += 1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Peça ao usuário para informar  números inteiros e em seguida informe quantos dos números são pares e quantos são ímpares

contador = 1
par = 0
impar = 0
while contador <= 3:
    num = int(input(f"Digite o {contador}º Número: "))
    if num %2 ==0:
        print(f"O  número {num} é par")
        par = par + 1
    else:
        print(f"O número {num} é impar")
        impar = impar + 1
    contador += 1
print(f"Foram {par} número(s) Par")
print(f"Foram {impar} número(s) Impar")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Imprima em tela a sequência de 0 até o número POSITIVO digitado pelo usuário.

num = int(input("Digite um número: "))

contador = 0
while contador <= abs(num):
    print(contador)
    contador += 1
 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Imprima em tela a sequência de 0 até o número NEGATIVO digitado pelo usuário.

num = int(input("Digite um número: "))

contador = 0
while contador <= num:
    print(contador * -1)
    contador += 1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Crie um programa que peça uma nota entre 0 e 10.
#Se o valor for diferente, informe que é inválido e peça novamente o número até que o usuário acerte.

while True:
    num = int(input("digite um numero: "))
    if 0 <= num <=10:
        break
    else:
        continue
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Escolha um número entre 1 e 10 e peça para que o usuário tente acertar este valor.
Informe se o palpite é maior ou menor que o número secreto.
Quando o número estiver correto, imprima uma mensagempara isso.'''

while True:
    num = int(input("Descubra o número, dica fica etre 1 e 10: "))
    segredo = 5
    if num > segredo:
        print("Você escolheu um numero maior que o segredo")
        continue
    elif num < segredo:
        print("Você escolheu um numero menor que o segredo")
        continue
    else:
        print("Voce acertou")
        break

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Refaça a questão anterior, porém, o número secreto será gerado pelo módulo RANDOM, e sua função RANDINT.
Lembretes:
É preciso importar a biblioteca random.
O randint precisa de um número de início e o fim.'''



import random
segredo = random.randint(1,10)
while True:
    num = int(input("Descubra o número, dica fica etre 1 e 10: "))
    if num > segredo:
        print("Você escolheu um numero maior que o segredo")
        continue
    elif num < segredo:
        print("Você escolheu um numero menor que o segredo")
        continue
    else:
        print("Voce acertou")
        break

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Peça 5 números e informe a soma de todos eles.'''

contador = 1
soma = 0
while contador <= 5:
    num = int(input(f'digite o {contador}º número: '))
    soma = soma + num
    contador += 1
print(soma)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Peça 5 números e informe a soma de todos eles e a média'''

contador = 1
soma = 0
while contador <= 5:
    num = int(input(f'digite o {contador}º número: '))
    soma = soma + num
    contador += 1
print(soma/5)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Peça vários números até o usuário decidir parar. Depois, informe a soma e a média deles.'''

contador = 1
soma = 0
media = 1
while True:
    num = int(input(f'digite o {contador}º número: '))
    parar= input("Deseja continuar? SIM/NÃO")
    contador += 1
    soma = soma + num
    if parar == "sim":
        media += 1
        continue
    else:
        break
print(soma/media)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''A sua empresa precisa de um sistema para calcular as médias das avaliações dos candidatos da nova entrevista.
Desenvolva um programa que peça 4 notas e depois calcule a média.'''

contador = 1
soma = 0
while contador <= 4 :
    num = int(input(f'digite a {contador}ª nota: '))
    contador += 1
    soma = soma + num
print(soma/4)




