"""""
Listas (list)

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
lista4 = list(range(15)) #gera inteiros de 0 a 14
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
#podemos remover facilmenteo último elemento de uma lista
print(lista5)
lista5.pop() #nao somento remove o ultimo elementos mas também o retorna
print(lista5)
lista5.pop(3) #remove o elemento pelo índice
#OBS: os elementos à direita seu deslocados para a esquerda
#OBS: o pop só remove o elemento no índice caso esse índice(posicao) exista, caso nao tenha
# dará um index error
print(lista5)

--------------------------------------------
#podemos remover facilmenteo último elemento de uma lista
print(lista5)
lista5.pop() #nao somento remove o ultimo elementos mas também o retorna
print(lista5)
lista5.pop(3) #remove o elemento pelo índice
#OBS: os elementos à direita seu deslocados para a esquerda
#OBS: o pop só remove o elemento no índice caso esse índice(posicao) exista, caso nao tenha
# dará um index error
print(lista5)

lista2.remove('A') #o remove remove um elemento escolhido
print(lista2)
--------------------------------------------

#podemos remover todos os elementos da lista (zerar)
print(lista5)
lista5.clear()
print(lista5)
--------------------------------------------

#Podemos repetir uma elementos em uma lista
nova = [1,2,3]
nova = nova*3
print(nova)
--------------------------------------------

#podemos converter uma string para uma lista
#Ex1:
curso = 'Programação em python: Essencial'
print(curso)
curso = curso.split()
print(curso)
#OBS: o split por padrao separa os elementos da lista pelo espaço entre elas

#Ex2:
curso = 'Programação,em,python:,Essencial'
curso = curso.split(',') #o separador pode ser referenciado no parâmetro
print(curso)
--------------------------------------------

lista6 = ['Programação', 'em', 'Python:','Essencial']
#convertendo uma lista em string
print(lista6)

#pega a lista6, coloca espaço entre cada elemento e transforma em string
curso = ' '.join(lista6) 
print(curso)

#pega a lista6, coloca cifrão entre cada elemento e transforma em string
curso = '$'.join(lista6)
print(curso)
--------------------------------------------

#podemos colocar qualquer tipo de dado em uma lista, mesmo misturando dados
lista6 = [1, 2, 34, True, 'Geek', 'd', [1, 2, 3], 4356789]
print(lista6)
print(type(lista6))
--------------------------------------------

#Iterando sobre listas
#Ex1: Usando for

soma = '' 
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)
#obs: dessa maneira, pega uma string e junta tudo

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)


#Ex2: usando while

#Cria uma variável do tipo lista
carrinhodecompras = []
#Cria uma variável do tipo string
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinhodecompras.append(produto)

for produto in carrinhodecompras:
    print('****')
    print(produto)
--------------------------------------------

#Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)
--------------------------------------------

#Fazemos acesso aos elementos de forma indexada 
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

#fazemos acesso aos elementos de forma indexada inversa
# O índice negativo funciona em uma lista em formato circular
# O final de um elemento está ligado ao inicio da lista

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])
print(cores[-5]) #indexerror porque nao existe índice -5
--------------------------------------------

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
--------------------------------------------

#Gerar indice em um for
for indice, cor, in enumerate(cores):
    print(indice, cor)

#listas aceitam valores repetidos
--------------------------------------------

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)
--------------------------------------------

##Outros métodos uteis mas nao tao importantes

#encontrar o índice de um elemento na lista
numeros = [5, 6, 7, 5, 8, 9, 10]

#em qual indice está o valor 6?
print(numeros.index(6))

#em qual indice está o valor 9?
print(numeros.index(9))

#OBS: caso nao tenha esse elmento na lista, será apresentado ValueError
#print(numeros.index(15))

#retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

#Podemos fazer uma busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1)) #buscando a partir do indice 1
print(numeros.index(5, 2)) #buscando a partir do indice 2
print(numeros.index(5, 3)) #buscando a partir do indice 3
#print(numeros.index(5, 4)) #buscando a partir do indice 4
#OBS: Caso nao encontre, ValueError

#podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) #busca o indice do valor 8 entre os indices 3 a 6
--------------------------------------------

#Revisao de slicing
#lista[inicio:fim:passo]
#range[inicio:fim:passo]

#Trabalhando com slicing de listas com o parametro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:]) #iniciando do indice 1 e pegando todos os restantes

#Trabalhando com slice da lista com parametro 'fim'

print(lista[:2]) #começa em 0, pega até o indice 2 - 1
print(lista[:4]) #começa em 0, pega até o indice 4 - 1
print(lista[1:3]) #começa em 1m pega até o indice 3 - 1

#Trabalhando em lista com slice de parâmetro 'passo'
print(lista[1::2]) #começa em 1, vai até o final de 2 em 2
print(lista[::2]) #começa em zero e vai até o final de 2 em 2
print(lista[1::-1]) #começa em 1, e inverter a lista
--------------------------------------------
#invertendo valores em uma lista
nomes = ['Geek', 'University']
nomes[0],nomes[1] = nomes[1], nomes[0]
print(nomes)
#ou mais fácil
nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)
--------------------------------------------
#Soma*, valor máximo*, valor mínimo*, Tamanho
#* Se os valores forem fotos inteiros ou reais.
lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) #soma
print(max(lista)) #Máximo valor
print(min(lista)) #Mínimo valor
print(len(lista)) #Tamanho da lista
--------------------------------------------
#Transformar lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
--------------------------------------------
#Desenpacotamento de listas

lista = [1, 2, 3]
num1, num2, num3 = lista
#OBS: Se tivermos mais elementos para desempacotar do que variáveis para receber valores,
# teremos ValueError, e o contrário também é verdadeiro.
print(num1)
print(num2)
print(num3)
--------------------------------------------
#Copiando uma lista para outra (Shallow Copy e Deep Copy)
#Forma 1: Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)
# Ao utilizar lista.copy() copiamos dados da lista para uma nova lista, mas elas
#Ficaram totalmente independentes, ou seja, modifica uma lista, mas nao a outra
#Em python isso se chama Deep copy (copia profunda)


#forma 2: Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista #cópia
print(nova)
nova.append(4)
print(lista)
print(nova)

#Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
#apos realizar modificação em uma das listas, a modificação se refletiu em ambas as listas
#Isso em python é chamado de Shallow copy
--------------------------------------------
"""""




