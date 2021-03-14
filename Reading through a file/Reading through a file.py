print ('Buscando a traves de un archivo')
file = open("ZOOM ID.txt")

for search in file:
    search = search.rstrip()#Elimina los espacios en blanco
    if search.startswith('ID') and search.endswith('8'):#Encuentra la coincidencia mas efectiva al inicio
        print(search)#arroja todo los resultados que comiencen con el criterio
       
        
#es posible realizar busquedas especificando la terminación endswith
