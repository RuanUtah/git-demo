"""""
Conjuntos

- Conjuntos em qualquer lingaugem de prog, estamos fazendo referência à teoria dos conjuntos 
da matemática

- Aqui no python, os conjuntos sao chamados de Sets.

Disto isto, da mesma forma que na matemática:
    - Sets não possuem valores duplicados;
    - Sets nao possuem valores ordenados;
    - Elementos não são acessados via índice, ou seja, conjuntos não são indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas 
não nos importamos com a ordenação deles. Quabndo não precisamos nos preocupar com chaves,
valores e itens duplicados.

Os conjuntos (sets) são referenciados em python com chaves {}

Diferença entre conjuntos (Sets) e Mapas (Dict):
    - Um dicionário tem chave e valor
    - Um conjunto tem apenas valor;
------------------------------------------------------------

#Definindo um conjunto

#Forma 1

S = set({1, 2,3 ,4 ,5, 6, 7, 2, 3}) #repare que temos valores repetidos
print(S) 
print(type(S))

#OBS: Ao criar um conjunto, caso seja adicionado um valor já existente,
#  o mesmo será ignorado sem gerar erro e não fará parte do conjunto.

#Forma 2 - m,ais comum

S = {1,2,3,4,5,5}
print(S)
print(type(S))

#Podemos verificar se determinado elemento está contido no conjunto

if 3 in S:
    print('Tem o 3')

else:
    print('Nao tem o 3')

------------------------------------------------------------
#Importante lembrar que além de não termos valores duplicados, não temos ordem

#Listas aceitam valores duplicados entao temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)}')

#Tuplas aceitam valores duplicados entao temos 10 elementos
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)}')

#Dicionarios nao aceitam valores duplicados entao temos 8 elementos
dic = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicio: {dic} com {len(dic)}')

#Conjuntos nao aceitam valores duplicados entao temos 8 elementos
s = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Set: {s} com {len(s)}')
------------------------------------------------------------
#Assim como todo outro conjunto Python, podemos colocar tipos de dados misturados em sets

s = {1, 'b', 'True', 34.22, 44}
print(s)
print(type(s))

#Podemos iterar em um set no0rmalmente

for valor in s:
    print(valor)
------------------------------------------------------------
#Usos interessantas com sets

#Imagine que fizemos um formulário de cadastro de visitantes de visitantes em uma feira ou museu
# e os visitantes informam manualmente a cidade de onde vieram.

#Nós adicionamos cada cidade em uma lista Pythonb, 
# já que em uma lista podemos adicionar novos elementos e ter repetição

cidades = ['Belo Horizonte', 'São paulo', 'Campo grande','Cuiaba','Campo grande', 'São paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

#Agora precisamos saber quantas cidades distintas temos
# O que você faria? Loop na lista?
# podemos utilizar o stet para isso:

print(len(set(cidades)))
------------------------------------------------------------
#Adicionando elementos em um conjunto

s = {1,2,3}

s.add(4)
s.add(4) #Duplicidade nao gera erro, simplesmente é ignorado.
print(s)
------------------------------------------------------------
#Remover elementos em um conjunto

s = {1,2,3}
print(s)

#Forma 1

s.remove(3) #informa o valor a ser removido
print(s)

#OBS: caso o valor n seja encontrado, será gerado erro KeyError, nenhum valor é retornado.

#Forma 2

s.discard(2) 
#s.discard(22)
#OBS: Se o valor não for encontrado, nenhum erro é gerado.
print(s)
------------------------------------------------------------
#Copiando um conjunto para outro

#Forma 1 - Deep copy
s = {1,2,3}
print(s)

novo = s.copy()
print(novo)

novo.add(4)

print(s)
print(novo)

#Forma 2 - Shallow copy
s = {1,2,3}
print(s)

novo = s

novo.add(4)
print(novo)
print(s)
------------------------------------------------------------
#Podemos remover todos os itens de um conjunto

s = {1,2,3}
s.clear()
print(s)
------------------------------------------------------------
#Métodos matemáticos de Conjunto

#Imagine que temso 2 conjuntos, um contendo estudantes do curso python
#  e um do curso de java

estudante_python = {'Marcos', 'patricia', 'Ellen', 'Pedro', 'julia', 'guilherme'}
estudantes_java = {'Fernando', 'gustavo', 'julia', 'ana', 'Patricia'}

#Veja qeu alguns alunos que estudam python, estudam Java

#Precisamos gerar um conjunto com nomes de estudantes únicos

#FOrma 1 - Union

unicos1 = estudante_python.union(estudantes_java)
#{'Patricia', 'julia', 'Marcos', 'Fernando', 'Pedro', 'patricia', 'ana', 'gustavo', 'Ellen', 'guilherme'}
print(unicos1)

#Forma 2 - Utilizando caractere pipe ' | '
uncos2 = estudante_python|estudantes_java

print(uncos2)
------------------------------------------------------------
#Gerar um conjunto de estudantes que estão em ambos os cursos

#Forma 1 - Intersection

ambos1 = estudante_python.intersection(estudantes_java)
print(ambos1)

#Forma 2 - Utilizando o &

ambos2 = estudante_python & estudantes_java
print(ambos2)
------------------------------------------------------------
"""""

estudante_python = {'Marcos', 'patricia', 'Ellen', 'Pedro', 'julia', 'guilherme'}
estudantes_java = {'Fernando', 'gustavo', 'julia', 'ana', 'patricia'}

# Gerar um conjunto que não esao no outro curso

so_python = estudante_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudante_python)
print(so_java)
