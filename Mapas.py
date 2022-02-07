"""""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em pyrthno são representados por chaves {}

------------------------------------------------------------
print(receita)
#Iterar sobre dicionários

for chave in receita: #Imprime as chaves
    print(chave)

for chave in receita: #Imrpime os valores
    print(receita[chave])


for chave in receita:
    print(f'{chave} : {receita[chave]}')
------------------------------------------------------------

#Acessando as chaves
print(receita.keys()) #printa as chaves somente

for chaves in receita.keys(): #imprime os valores - Mais recomendado
    print(receita[chaves])
------------------------------------------------------------
#Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)
------------------------------------------------------------

#Desempacotamento de dicionarios

print(receita.items())

for chaves, valor in receita.items():
    print(f'chave={chaves} e valor {valor}')
------------------------------------------------------------


"""""

from optparse import Values


receita = {'jan':100,'fev':250,'mar':400}

#Soma*, valor Max*, Valor Min*, Tamanho

#* só pode usar valores reais ou inteiros

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

