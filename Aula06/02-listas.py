''' crie uma lista com valores variados e envie a mesma para uma função que irá imprimir essa lista'''

nomes = ["Lucas", "Mateus", 22, 1992, "Flavio"]
def imprimir (lista):
    print(lista)

imprimir(nomes)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# as listas possuem indices

'''Como as listas possuem diversos valores, podemos acessar ou modificar o item de uma
lista acessando o seu índice. O primeiro índice da lista sempre inicia com 0 e termina com a
quantidade de itens da lista -1. Também podemos acessar o último item de uma lista que
começa com -1. '''

#para acesse um item especifico na lista colocamos o numero do indice dentro dos colchetes

nomes = ["Lucas", "Mateus", 22, 1992, "Flavio"]
nomes[0] '''Lucas'''

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Crie uma função que irá receber duas listas de valores inteiros e irá imprimir a
soma do item do primeiro índice da primeira lista, com o último item da segunda
lista'''
primeira_lista = [1,2,3,4,5,6,7,8,9,10]
segunda_lista = [10,9,8,7,6,5,4,3,2,1]

def soma(lista_1, lista_2):
    operacao = lista_1 + lista_2
    return operacao

resultado = soma(primeira_lista[0], segunda_lista[-1])

print(f'a soma do primeiro item da primeira lista e o '
      f'último item da segunda lista é {resultado}')

'''resposta do professor'''


lista1 = [1,2,3,4]
lista2 = [4,5,6,9]

def somar(lista1, lista2):
    resultado = lista1[0] + lista2[-1]
    print(f'Resultado da soma: {resultado}')

somar(lista1,lista2)



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Crie uma lista com 5 valores inteiros variados. E crie uma função que irá receber
essa lista e imprimir a soma de todos os valores da lista'''

numero = [1,2,3,4,5]

def soma(lista):
    soma_lista = sum(lista)
    return soma_lista

print(soma(numero))

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Fatiamento de Lista
[inicio:fim:step]


#append(): vai adidionar um item no final da lista
#insert(posição, valor): igual a função append, porem eu posso escolher onde o novo item vai ser acrescentado.



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Crie uma função que irá ler 5 valores e inseri-los em uma lista e em seguida
exiba-os na tela'''

def valor():
    contador = 1
    lista = []
    while contador <= 5:
        numero = input(f"Digite o {contador}º numero: ")
        lista.append(numero)
        contador = contador + 1
    print(lista)

valor()

# resposta do professor

def inserir_na_lista():
    lista = []
    for i in range(5):
        valor = input('Informe o valor: ')
        lista.append(valor)

    print(lista)

inserir_na_lista()


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Crie uma função que irá ler três notas, em seguida armazene-as em uma lista.
Em seguida realize a média desses valores contidos nessa lista. '''

def media():
    contador = 1
    lista_notas = []
    while contador <= 3:
        notas = float(input(f'Ditite a {contador}ª nota: '))
        lista_notas.append(notas)
        contador += 1
    calcular_media = sum(lista_notas)/3
    print(f'A média das notas é : {calcular_media:.2f}')
media()
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  














