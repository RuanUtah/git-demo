"""""
Dicionários

#OBS: em algumas linguagens de prog, os dicionários python são conhecidos por mapas.

Dicionários são coleções do tipo chave/ valor.
#É um mapeamento entre chave e valor

#Ideia de chave e valor em listas, isto é, índices e valores
[0,1,2]
[1,2,3]

#Nos dicionarios, isso fico explicito ao em vez de implícita

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre os dicionários
    - Chaves e Valor são separados por dois pontos 'chave': 'valor'
    - Tanto chave quanto valor podem ser de quaquer tipo de dado
    - podemos misturar tipos de dados
lista = []
tupla = ()
dicionario = {}
------------------------------------------------------------

#Criação de dicionários

#FOrma 1(Mais comum)
paises = {'br': 'Brasil','eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

#Forma 2(Menos comum)

paises = dict(br='Brasil', eua = 'Estados Unidos', py = 'Paraguay')
print(paises)
print(type(paises))
------------------------------------------------------------

#Acessando elementos

#Forma 1- Acessando via chave, da msm forma que lista/ tupla
paises = dict(br='Brasil', eua = 'Estados Unidos', py = 'Paraguay')

print(paises['br'])
print(paises['py'])
#print(paises['ru']) #Error
#OBS: Caso tentamos fazer um acesso utilziando uma chave que nao eixte, teremos o erro KeyError

#Forma 2 - Acessando via get - RECOMENDADO

print(paises.get('br'))
print(paises.get('ru'))
------------------------------------------------------------

russia = paises.get('ru', 'Nao encontrado')
#Caso o get nao encontre o objeto com a chave informada sera etornado o valor nonne e nao sera 
gerado KeyError.

if russia:
    print('Encontrei')
else:
    print('Nao encontrei')

print(f'Encontrei o país {pais}')

pais = paises.get('ru', 'Nao encontrado')
------------------------------------------------------------
#podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos ' in paises) #Ele nao busca o valor, ele busca a chave, por isso falso

if 'ru' in paises:
    russia = paises['ru']
------------------------------------------------------------
#podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, 
#tupla dicionarios, como chaves de dicionários

#Tuplas por ex são bastantes interessantes de serem utilizados como chave de dicionários
#pois sao imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em NY',
    (37.7749, 122.4194): 'Escritório em SP'
}

print(localidades)
print(type(localidades))
------------------------------------------------------------
#Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120,'mar': 300}
print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

#Forma 2 

novo_dado = {'mai':500}
receita.update(novo_dado) #receita.update({'mai':500})
print(receita)

#Atualizando dados em um dicionario

#Forma 1

receita['mai'] = 550

print(receita)

#Forma 2

receita.update({'mai':600})
print(receita)

#Conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma
#Conclusão 2: Em dicionarios, NÃO podemos ter chaves repetidas
------------------------------------------------------------
# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120,'mar': 300}
print(receita)

# Forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)
print(receita)
#OBS1: Aqui precisamos semrpe informar a chaver, e caso nao encontre o elemento, um KeyError é retornado

#OBS2: Ao removermos um objeto, o valor desde objeto é sempre retornado.

#Forma 2

del receita['fev']

print(receita)

#Se a chave não exister, será gerado um KeyError 
# Neste caso o valor removido nao é retornado
------------------------------------------------------------

#Imagine que voce tem um comercio eletronico, onde temos um carrinho de compras 
# na qual adicionamos produtos
"""""
"""""
Carrinho de compras:
    Produto_1:
        -nome;
        -quantidade;
        -preço;
    Produto_2:
        -nome;
        -quantidade;
        -preço;
"""""
"""""
# 1 poderiamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstation4' ,1, 2300.00]
produto2 = ['God of war', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Teriamos que saber qual é o índice de cada informação no produto.

# 2 poderiamos utilizar uma tupla para isso? Sim

carrinho = ()

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of war 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

#Teriamos que saber qual é o índice de cada informação no produto

# 3 - poderiamos tuilizar um dicionario para isso? Sim

carrinho = []

produto1 = {'Nome': 'Playstation 4','quantidade': 1, 'preço': 2300.00}
produto2 = {'Nome': 'God of war 4','quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Desta forma, facilmente adicionamos ou removemos prodyutos no carrinho em cada produto
# podemos ter a carteza sobre cada informação
------------------------------------------------------------
# Métodos de diconarios

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário

d.clear()
print(d)

# Copiando um dicionario para outro

#Forma 1

novo = d.copy() #Deep copy
print(novo)

novo['d'] = 4
print(d)
print(novo)

#Forma 2 - Shallow copy

novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)

"""""

#Forma nao usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))
#É criado um dicionario a partir de caracteres/ strings, em que 'a' é a chave e 'b' o valor

usuario = {}.fromkeys(['nome', 'pontos', '1email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))
#Nesse exemplo, é criado chaves dentro da lista, e 'desconhecido' se torna valor de cada chave
# O método fromkeys recebe dois parâmetros, um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a estra chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)
#Como cada caracter é um iterável, ele pegou cada letra da palavra teste e repetiu em valor, 
# nao houve repetição do resto de teste pq ja foi repetido

veja = {}.fromkeys(range(1,11), 'novo')
print(veja)
#Cada número será uma chave e seu valor correspondente será 'novo'