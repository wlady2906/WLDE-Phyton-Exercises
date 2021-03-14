print ('Determinar si un año es bisiesto con una función')

x = int(input('Introduce un año: '))
if x%4 == 0 and x % 100 == 0 and x % 400 == 0:
    print('El año es bisiesto')
else:
    print('El año no es bisiesto')
