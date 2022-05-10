import random

print("Digite a data de hoje")

data1 = input("Dia: ")
dia = int(data1)
data2 = input("Mes: ")
mes = int(data2)
data3 = input("Ano: ")
ano = int(data3)

print("Data: {:02d}/{:02d}/{:4d}".format(dia, mes, ano))



print("Dia {:02d} do mes {:02d} do ano {}".format(random.randrange(1, 32), random.randrange(1, 13), random.randrange(1901, 2101)))