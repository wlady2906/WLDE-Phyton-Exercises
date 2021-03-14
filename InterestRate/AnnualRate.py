'''

Programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. 
Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años 
si cada año se aplica la tasa de interés introducida.
Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en 
C * (1 + x/100)elevado a n (años). 
Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual 
se convierte en 24117.14 dolares al cabo de 20 años.

'''

import math

print ('Calcula la inversión con un interes anual')

usd = int(input('Cantidad de dolares que deseas invertir: '))
ts = float(input('Tasa de interés anual: '))
n = int(input('Número de años: '))

for x in range(1,n+1):
    C = usd * (1 + (ts/100)) ** x

print('La inversión al cabo de 20 años es de: ', C)
