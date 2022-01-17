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
"""""
#Problema 1011
pi = 3.14159
r = int(input(""))
v = (4/3.00)*pi*(r**3)
print('VOLUME = %.3f' % v)
"""""
"""""
#Problema 1012
pi = 3.14159
a,b,c = input().split(" ")
A = float(a)
B = float(b)
C = float(c)
ST = (A*C)/2
SC = pi*(C**2)
STRAP = ((A+B)*C)/2
SQ = B**2
SR = A*B
print('TRIANGULO: %.3f' % ST)
print('CIRCULO: %.3f' % SC)
print('TRAPEZIO: %.3f' % STRAP)
print('QUADRADO: %.3f' % SQ)
print('RETANGULO: %.3f' % SR)
"""""
"""""
#Problema 1013
A,B,C = input().split(" ")
a=int(A)
b=int(B)
s=int(C)
MaiorAB = ((a+b+(a*b*s)*(a-b)))/2
if a>b and a>s:
    print(f'{a} eh o maior')
if b>a and b>s:
    print(f'{b} eh o maior')
if s>a and s>b:
    print(f'{s} eh o maior')
"""""
"""""
#Problema 1014
X = int(input())
Y = float(input())
C = X/Y
print(f'{C:.3f} km/l')
"""""
"""""
#Problema 1015
a,b = input().split(" ")
x1 = float(a)
y1 = float(b)
c,d = input().split(" ")
x2 = float(c)
y2 = float(d)
dist = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)
print(f'{dist:.4f}')
"""""
"""""
#Problema 1015
X = 60
Y = 90
delt = 1/2
dist = int(input())
tempo = dist/delt
print(f'{tempo:.0f} minutos')
"""""

