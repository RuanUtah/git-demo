"""""
Dir -> Conjuntos de comandos que podem utilizar em relação à variável

Help -> Como utilizar e como funciona
------------------------------------------------------------
#Tipo Int
# Tipo real, inteiro.
a = int(input("Digite um número: "))
type(a)
print(a)
print(type(a))

# 5+4 ; 7-2; 3*5; 5/2; 5//2; 4%2; 5%2; 7%2; 2**3; 2**8; num +=1; num -=1; num *=2
------------------------------------------------------------
Tipo Float 
#Tipo real, decimal
#OBS1: Valor = 1,44 (Errado); 
b = float(input("Digita um número decimal: "))
type(b)
print(b)
print(type(b))
#Conversão float em inteiro
valor = 1.2
res = int(valor)
print(type(res))
#perde precisão

#OBS2: Podemos trabalhar com complexos
c = 1j
print(type(c))
dir(c)
------------------------------------------------------------
Tipo Booleano
#Verdadeiro ou falso; True e False

ativo = False 
print(ativo)
print(type(ativo))
Operação básicas: 

# Negação (not):
Fazendo a negação, se o valor booleano for verdadeiro o resultado será faldo, 
se for falso o resultado será verdadeiro. Ou seja sempre o contrário 
print(not ativo). 


Ou (or)
logado = False

Operação que envolve 2 valores, uma ou outro pode estar correto/ verdadeiro 

True or Ture -> True 
True or False -> True
False or True -> True
Flase or False -> False

print(ativo or logado)

E (and):
# tamgbém é uma operação binária, ou seja depende de dois valores. Ambos valores devem ser 
verdadeiros
True and True -> True
True and False -> False
False and true -> False
False and False -> False

5>6; 6>5; 6==6; 3<=5; num = 12 num2 = 14 num2>num1; 

É (is):
#Ativo é verdadeiro? 
ativo = True
print(ativo is True)
------------------------------------------------------------
Tipo String
# As strings são sequências de caracteres, de forma que podemos acessar 
um caractere em uma dada posição utilizando um índice 
# Tudo que tiver entre áspas simples ou duplas ou triplas; 'Ruan Utah', "Seu Presida", '''Lindo'''
nome = "Vitor Mendes"
print(nome)
print(type(nome))

nome = 'Vitor \n Mendes'
print(nome)

print(nome.lower())
print(nome.upper())
print(nome.split())

0 1 2 3 4 5 6 7
R u a n U t a h

nome = "Ruan Utah"
print(nome[0:7]) #Slice 
print(nome[::-1]) #Comece do primeiro, até o ultimo e inverta
print(nome.replace('a', 'v'))
------------------------------------------------------------
Condicionais

#If, else, elif

if variavel comparação valor: 
    comando


idade = 6
if idade < 18:
    print('Menor idade')
elif idade==18:
    print('Tem 18')
else: 
    print('Maior de idade')

Atividade: Jokenpô
tesoura > papel papel > pedra pedra > tesoura 
------------------------------------------------------------
Estrutura de repetição em python

# For, while, ranges, breaks

FOR: 
for variavel in range (início, fim):
    comando

i=0
for i in range(0, 6):
    print(i)
    i += 1
    print("Hello")

nome = "Ruan Utah"
for letra in nome:
    print(nome, end='')

OBS# Enumerate é utilizado para saber o índice de cada variável
for i, v in enumerate(nome):
    print(nome[i])
    #print(v)

for value in enumerate(nome):
    print(value)

qtd = int(input("Digite um número: "))
for n in range(1, qtd+1):
    print(f'Imprimindo {n}')


RANGES: 
# Utilizado para sequência númericas, de maneira específica. 
# Valor_de_parada não inclusive (ínicio de 0)
formas de uso: 

Forma 1: # Valor_de_parada(de 0 a um valor)
for num in range(11):
    print(num)

Forma 2: #(Valor_de_entrada, valor_de_saída)
for num in range (4,11):
    print(num)

Forma 3: #(Valor_de_entrada, valor_de_saída-1, passo)
for num in range (4,11,2):
    print(num)
"""""
