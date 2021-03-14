print ('Juego Master Mind, Adivinando la cadena')

cadena = 'A Random Word'
longitud = int(input('Dime la longitud de la cadena (2 a 9 digitos): '))

if longitud > 10:
    print('la cantidad de digitos no puede ser mayor a 10')
else:
    subcadena = cadena[0:longitud]
    print(subcadena)
    
print('Intenta adivinar la cadena....')
adivina = input()

count = 0
while count != len(subcadena):
    for x in range(len(subcadena)):
        if subcadena[x] == adivina[x]:
            count += 1
        elif count != len(subcadena):
            print('Has adivinado ', count, 'Valores. Intenta otra vez: ')
            count = 0
            adivina = input()
        elif count == len(subcadena):
            print('Has adivinado ', count, 'Valores. Felicidades ')
