import math

print ('Calcula la inversión con un interes anual')

usd = int(input('Cantidad de dolares que deseas invertir: '))
ts = float(input('Tasa de interés anual: '))
n = int(input('Número de años: '))

for x in range(1,n+1):
    C = usd * (1 + (ts/100)) ** x

print('La inversión al cabo de 20 años es de: ', C)
