x = input('Año en el que transcurre este programa ')
lista = [['Leidy','1996'],['Wladimir','1996'],['Stefanny', '2001']]
filas = 3;
columnas = 2;
for n in range(filas):
    for m in range(columnas):
       resta = int(x) - int(lista[n][1])
    print('Los años que cumplen al presente año ', resta)
