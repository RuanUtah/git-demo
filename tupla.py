"""""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.
Existem basicamente 2 diferenças básicas
1 - As tuplas sao representadas por parenteses ()
print(type(()))

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela nao muda. Toda
alteração em uma tupla gera uma nova tupla
--------------------------------------------

#CUIDADO 1: As tuplas são representadas por (), mas veja:
tupla1 = (1,2,3,4,5,6)
print(tupla1)
print(type(tupla1))

tupla2 = 1,2,3,4,5,6
print(tupla2)
print(type(tupla2))

#OBS: O python por padrao reconhece uma representação de dados mesmo sem parenteses como uma tupla

#CUIODADO 2: Tuplas com 1 elemento

tupla3 = (4) #Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4, ) #isso é uma tupla
print(tupla4)
print(type(tupla4))

#Podemos concluir que as tuplas são definidas pela vírgula e não pelo uso do parênteses

tupla5 = 4,
print(tupla5)
print(type(tupla5))

(4) -> Não é tupla
(4, ) -> è uma tupla
4, -> é uma tupla
--------------------------------------------
#Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))
--------------------------------------------
#Desempacotamento de tupla

tupla = ('Geek university', 'Programação em Python: Essencial')
escola, curso = tupla
print(escola)
print(curso)

#OBS: Gera um ValueError se colocarmos um numero diferente de elementos e variáveis para desempacotar
--------------------------------------------
#Métodos para Adicação e remoção de elementos de tuplas não existem, dado o fato delas serem imutaveis
#Soma*, Valor Máximo*,Valor mínimo* e Tamanho

#* Se os valores forem todos inteiros ou reais
tupla = (1,2,3,4,5,6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
--------------------------------------------

"""""

