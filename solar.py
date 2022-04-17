from matplotlib import pyplot as plt 

# 
x = 1
i = 1
contas_dos_meses = []

qtd = int(input("Quantos meses a registrar?: "))
meses = range(1,qtd+1)
for i in range (1, qtd+1):
    print(f'conta do mes {i}: ')
    x = int(input(""))
    contas_dos_meses.append(x)
    print(x)

print(contas_dos_meses)
plt.plot (contas_dos_meses, meses)