"""""
Saindo de loops com break

funciona igualmente como em C/C++
>> Usado para sair de loops de maneira projetada

#Ex 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')

#Ex 2
while True:
    comando = input('Digite sair para sair: ')
    if comando == 'sair':
        break
"""""
#Ex 2
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')