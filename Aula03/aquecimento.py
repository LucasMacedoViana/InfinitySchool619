'''Aquecimento 01:
1) Peça um nome
2) Peça o sobrenome
Imprima o nome e o sobrenome utilizando
F-STRINGS'''

nome = str(input("Digite seu nome: "))
sobrenome = str(input("digite seu sobre nome: "))

print(f"{nome} {sobrenome}")

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Aquecimento 02:
1) Peça um número inteiro e positivo
2) Peça outro número inteiro e positivo
Construa uma CALCULADORA com as
operações básicas: soma, subtração,
multiplicação e divisão.
Obs: o usuário que irá escolher a operação!'''

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numeor: "))
operacao = int(input("Qual operação você deseja fazer?"
                 "\n1- somar"
                 "\n2- subtrair"
                 "\n3- multiplicar"
                 "\n4- dividir: "
                 "\n"))

somar = num1 + num2
subtrair = num1 - num2
multiplicar = num1 * num2
dividir = num1 / num2

if operacao == 1:
    print(f" {num1} + {num2} = {somar:.2f}")
elif operacao == 2:
    print(f"{num1} - {num2} = {subtrair:.2f}")
elif operacao == 3:
    print(f"{num1} x {num2} = {multiplicar:.2f}")
elif operacao == 4:
    print(f'{num1} / {num2} = {dividir:.2f}')
else:
    print("ATENÇÃO NA ESCOLHA DA OPERAÇÃO")
'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Aquecimento 03:

1) Peça o usuário
2) Peça a senha
Se o usuário for admin e a senha 619:
acesso liberado, senão, acesso bloqueado.'''

login = input("Usuário: ")
senha = int(input("senha: "))

if (login.lower() == "admin") and (senha == 619):
    print("Acesso liberado")
else:
    print("Acesso negado")
'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Aquecimento FINAL:

Crie um código que informe ao usuário se
o número digitado é PAR ou ÍMPAR.'''

num = float(input("Informe o número: "))

resultado = num % 2

if resultado == 0:
    print(f"O número {num} é Par ")
else:
    print(f"O número {num} é Impar ")
'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------'''    
    

