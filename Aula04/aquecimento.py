'''01- Peça para o usuário digitar dois nomes e imprima o maior deles utilizando F-STRING.'''

nome1 = input("1º nome: ")
nome2 = input("2º nome: ")

if nome1 > nome2:
    print(f"{nome1}")
else:
    print(f"{nome2}")
