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
#Podemos facilmentar contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista2.count('A'))

# Para adicionar elementos em listas, utilizamos a função append
lista1.append(10) #append coloca um elemento na última posição por vez
print(lista1)

lista1.insert(2,10) #insert coloca um elemento na posição determinad, deslocando elementos para direita
print(lista1)
#OBS: lista1.append(10, 15, 20, 30) = erro, só pode um por vez

lista1.append([8,3,1]) #pode colocar uma lista dentro de uma lista
print(lista1)

if [8,3,1] in lista1:
    print('Encontrado [8,3,1]') #verifica o conjunto

lista1.extend([123,44,67]) #coloca a lista como elemento único (sublista)
print(lista1)
--------------------------------------------
#podemos facilmente juntar duas listas
lista6 = lista1+lista2
#lista1.extend(lista2)
print(lista1)
--------------------------------------------
#Podemos inverter uma lista
#Forma 1
lista1.reverse()
lista2.reverse()

#Forma 2
print(lista1[::-1])
print(lista2[::-1])
--------------------------------------------
#Copiar uma lista
lista6 = lista2.copy()
print(lista6)
--------------------------------------------
#Podemos contar quantos elementos existem na lista
print(len(lista2))
--------------------------------------------

--------------------------------------------

--------------------------------------------

--------------------------------------------

--------------------------------------------
"""""

lista1 = [1,3,4,2,7,9,5,6,8,10] #inteiro
lista2 = ['R','U','A','N','','U','T','A','H'] #caracteres = string
lista3 = []
lista4 = list(range(15)) #gera inteiros de 0 a 10
lista5 = list('Ruan Utah') #lista5 igual a lista2

#podemos remover facilmenteo último elemento de uma lista
print(lista5)
lista5.pop() #nao somento remove o ultimo elementos mas também o retorna
print(lista5)
lista5.pop(3) #remove o elemento pelo índice
#OBS: os elementos à direita seu deslocados para a esquerda
#OBS: o pop só remove o elemento no índice caso esse índice(posicao) exista
print(lista5)


#lista5.remove('a') #o remove remove um elemento escolhido e todas suas cópias na lista
#print(lista5)

