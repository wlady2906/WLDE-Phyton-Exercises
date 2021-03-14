print ('Lista con conjunto de nombres y con letra a buscar')

nombres = ['Amelia','Shiki','Charlotte','Monica','Silvia','Carla','Jose','Wladimir','Leidy']

x = input('Introduce la letra con la que deseas buscar el nombre: ')
count = 0

for search in range(len(nombres)):
    #Usamos la funcion startswith para establecer el criterio de búsqueda
    if nombres[search].startswith(x) or nombres[search].startswith(x) :
        count += 1
        print(nombres[search])
print('Cantidad de nombres con letra ',x ,' encontrada: ', count)   
