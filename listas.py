"""""
Listas

>> Listas em python funciona como vetores/ matrizes (arrays) em outras linguagens,
com a diferença de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo, ou seja, um array do tipo int sempre será int
    e tamanho definido
Python:
    - Dinâmico: Não possui tamanho definido, pode ir criar lista e simplesmente adicionar elementos,
--------------------------------------------
lista1 = [1,2,3,4,5,6,7,8,9,10] #inteiro
lista2 = ['R','U','A','N','','U','T','A','H'] #caracteres = string
lista3 = []
lista4 = list(range(15)) #gera inteiros de 0 a 10
lista5 = list('Ruan Utah') #lista5 igual a lista2

#Podemos facilmente checar se determinado valor está contido na lista
#Ex1:

num = int(input(''))
if num in lista1:
    print(f'Encontrei o número {num}... ')
else:
    print(f'Nao encontrado o número {num}... ')


# podemos facilmente ordenar uma lista 
lista1.sort()
print(lista1)

--------------------------------------------



"""""

lista1 = [1,3,4,2,7,9,5,6,8,10] #inteiro
lista2 = ['R','U','A','N','','U','T','A','H'] #caracteres = string
lista3 = []
lista4 = list(range(15)) #gera inteiros de 0 a 10
lista5 = list('Ruan Utah') #lista5 igual a lista2



# podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)
