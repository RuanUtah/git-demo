"""""
#Problema 1002
pi = 3.14159
r = float(input(""))
S = pi*(r**2)
print('A=',end='')
print("%.4f" %S)
"""""
"""""
#Problema 1003
A=int(input(""))
B=int(input(""))
SOMA = A+B
print('SOMA =',SOMA)
"""""
"""""
#Problema 1004
A=int(input(""))
B=int(input(""))
PROD = A*B
print('PROD =',PROD)
"""""
"""""
#Problema 1005
A=float(input(""))
B=float(input(""))
PA = A*3.5
PB = B*7.5
MEDIA = (PA+PB)/11
print('MEDIA = %.5f' % MEDIA)
"""""
"""""
#Problema 1006
A=float(input(""))
B=float(input(""))
C=float(input(""))
PA = 2*A
PB = 3*B 
PC = 5*C
MD = (PA+PB+PC)/10 
print("MEDIA = %.1f" %MD)
"""""
"""""
#Problema 1007
A=int(input(""))
B=int(input(""))
C=int(input(""))
D=int(input(""))
Dif = (A*B)-(C*D)
print('DIFERENCA =',Dif)
"""""
"""""
#Problema 1008
N=int(input(""))
NHT=int(input(""))
VH=float(input(""))
SAL = VH*NHT
print('NUMBER =',N)
print("SALARY = U$ %.2f" %SAL)
"""""
"""""
#Problema 1009
NAME = input("")
SF=float(input(""))
TV=float(input(""))
COM = 0.15*TV
TOT = SF+COM
print("TOTAL = R$ %.2f" % TOT)
"""""
"""""
#Problema 1010
COD1,NUM1,VUNIT1 = input().split(" ")
COD1 = int(COD1)
NUM1 = int(NUM1)
VUNIT1 = float(VUNIT1)
COD2,NUM2,VUNIT2 = input().split(" ")
COD2 = int(COD2)
NUM2 = int(NUM2)
VUNIT2 = float(VUNIT2)
VP = (NUM1*VUNIT1) + (NUM2*VUNIT2)
print('VALOR A PAGAR: R$ %.2f' %VP)
"""""