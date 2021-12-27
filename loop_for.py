"""""
nome = "Ruan Utah"
lista = (1, 3, 5, 9)
numeros = range(1, 10)

for letra in nome:
    print(letra)
------------------------------
nome = "Ruan Utah"
lista = (1, 3, 5, 9)
numeros = range(1, 10)

for letra in nome:
    print(letra, end = '') #coloca a estrutura numa linha só
------------------------------
for i, v in enumerate(nome):
    print(nome[i]) # print o conteudo da posicao
------------------------------
for _, v in enumerate(nome):
    print(v) # caso tenha valores descartáveis, pode ser usado o '' _ ''
------------------------------
for v in enumerate(nome):
    print(v)  # print o índice e o valor do índice
------------------------------
qtd = int(input('Quatas vezes rodar? '))

for n in range (1, qtd+1):
    print(f'imprimindo {n}') # looping de for printando até o numero requesitado
------------------------------
"""""

qtd = int(input('Quatas vezes rodar? '))

for n in range (1, qtd+1):
    print(f'imprimindo {n}')



