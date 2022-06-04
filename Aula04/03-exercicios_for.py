'''01-Imprima em tela a sequência de 0 até 50.'''

for num in range (0,51):
    print(num)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''02- Imprima em tela a sequência de 100 até 0.'''
for num in range (-100, 1):
    print(num * -1)
    
 '''ou'''
for num in range (100, -1, -1):
    print(num)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''03- Peça 5 números e informe a soma de todos eles e a média'''

soma = 0
for num in range (1, 6):
    valor = float(input(f"digite o {num}º número: "))
    soma = soma + valor
media = soma / 5
print(media)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''04- Crie um programa que peça dez números inteiros e positivos.
Ao finalizar, informe separadamente o valor da soma dos números pares e dos números ímpares.'''

par = 0
impar = 0
for contador in range (1, 11):
    valor = float(input(f"digite o {contador}º número: "))
    if valor % 2 ==0:
        par += valor
    else:
        impar += valor
print(f"A soma dos pares {par}")
print(f"A soma dos impares {impar}")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''05- Solicite ao usuário um limite inferior e um superior, depois informe quantos números pares existem no intervalo.'''
inicio = int(input("digite o inicio: "))
fim = int(input("digite o final: "))
pares = 0
for contador in range (inicio, fim +1):
    if contador % 2 == 0:
        pares +=1
print(pares)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''06- Crie um algoritmo que imprima na tela os números de 1 a 10, sendo primeiramente os números pares e, em seguida, os ímpares.'''

inicio = 1
fim = 11
print("pares")
for contador in range (inicio, fim):
    if contador % 2 == 0:
        print (contador)

print("impares")
for contador in range (inicio, fim):
    if contador % 2 != 0:
        print (contador)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
