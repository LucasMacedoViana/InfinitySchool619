def nome da função (parametros ou argumentos):
  Corpo da função
  
def somar(valor_1,valor_2):
    print(f'{valor_1 + valor_2}')

somar(10,10)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def area_circulo(raio):
    pi = 3.14
    circulo = pi *(raio ** 2)
    return circulo // devolve o resultado da função

area = area_circulo(5)

print(f'{area}')

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Criem uma função que recebe o login e a senha do usuario

- login = 'administrador' e a senha = 'escola'
print usuario autenticado

se incorreto
printar dados invalidos'''

def acesso():
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == "administrador" and senha == "escola":
        print("Usuario autenticado")
    else:
        print("Dados invalidos")

acesso()

ou
'''(resposta do professor)'''
def autenticar(login, senha):
    if login == 'administrador' and senha == 'escola':
        print('Dados corretos!!')
    else:
        print('Dados inválidos!!')

username = input('Digite seu login: ')
password = input('Digite sua senha: ')

autenticar(username, password)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Criem uma função chamada calculadora

valor1, valor, e o operador

se o operador = '+'
Somar os dois valores
e retornar o resultado

Se o operador = '*'
Multiplicar os dois valores
e retornar o resultado

Se o operador = '/'
Dividir os dois valores
e retornar o resultado

Se o operador = '-'
Subtrair os dois valores
e retornar o resultado

Se não for nenhum dos operadores acima informar que o operador é invalido'''

def calcular():
    num1 = float(input("1º número: "))
    num2 = float(input("2º número: "))
    operador = input("(+) soma"
                     "\n(-) subtração"
                     "\n(/) divisão"
                     "\n(*) multiplicação"
                     "\nDigite a operação: ")

    if operador == "+":
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operador == "-":
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operador == "/":
        print(f'{num1} / {num2} = {num1 / num2}')
    elif operador == "*":
        print(f'{num1} x {num2} = {num1 * num2}')
    else:
        print("Operador Invalido") 

calcular()

ou
'''(resposta do professor)'''
def calculadora(valor1, valor2, operador):
    if operador == '+':
        return valor1 + valor2
    elif operador == '/':
        return valor1 / valor2
    elif operador == '*':
        return valor1 * valor2
    elif operador == '-':
        return valor1 - valor2
    else:
        return 'Operador é inválido'
    
print(f'Resultado da soma: {calculadora(10, 2, "+")}')
print(f"Resultado da multiplicação: {calculadora(10, 2, '*')}")
print(f"Resultado da divisão: {calculadora(10, 2, '/')}")
print(f"Resultado da subtração: {calculadora(10, 2, '-')}")
print(f"Resultado inválido: {calculadora(10, 2, '@')}")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Joaozinho ele possui um carro que faz 12km/l. Criem uma função que vai calcular o consumo de gasolina do carro dele. Vocês precisam informar duas entradas, o tempo (em horas) que ele dirigiu e a velocidade que ele fez esse percurso. '''


''' 12 é o consulmo do carro 12km/l'''
def consulmo (velocidade, tempo):
    distancia = velocidade * tempo
    litros = distancia / 12
    return litros

print(consulmo(24, 2))

ou 
'''(resposta do professor)'''

