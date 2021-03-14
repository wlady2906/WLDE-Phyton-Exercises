print ('Ingresa una cadena para veriguar el numero de letras mayusculas')

#Le pedimos al usuario que introduzca una cadena
x = input('Introduce una cadena de caracteres ')
mayus = 0 #contador para las mayusculas

#Realizamos un bucle for para recorrer la cadena
for i in range(len(x)):
    cadena = x
    if cadena[i].isupper() == True:
        mayus = mayus + 1
print('la cantidad de mayusculas es de ', mayus)
