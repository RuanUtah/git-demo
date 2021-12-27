"""""
Ranges sao utlizados para gerar sequencia numericas nao de forma aleatória,
mas sim de maneira especificada.
-------------------------------
#forma 1
range(valor_de_parada)
obs: Valor_de_parada nao é incluso

Ex: for num in range(11):
    print(num)
-------------------------------
#forma 2

range(valor_de_inicio, valor_de_parada)
obs: valor_de_parada nao incluso (inicio especificado pelo usuario)
Ex: for num in range(1, 11):
    print(num)
-------------------------------
# Forma 3
range(valor_de_inicio, valor_de_parada, passo)
obs: valor_de_parada nao incluso (inicio especificado pelo usuario, e passo especificado pelo mesmo)
Ex: for num in range(1, 10, 2):
    print(num)

#Forma 4
range(valor_de_inicio, valor_de_parada, passo)
obs: valor_de_parada nao incluso (inicio especificado pelo usuario, e passo especificado pelo mesmo)
Ex: for num in range (10, 1, -1):
    print(num)

lista = list(range(10))
print (list) # gera uma lista a partir de um range
"""""

for num in range (10, 1, -1):
    print(num)
