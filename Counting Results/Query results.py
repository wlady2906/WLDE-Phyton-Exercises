print ('Searching for a filename and specify query results')
desk = input('Search for a file --> ')# Criterio de busqueda

try:
    #Si coinciden los criterios
    abrir = open(desk) #abre el criterio de busqueda
except:
    #Si no coinciden los criterios
    #En caso de escribir mal el nombre de un archivo
    print("File not found, ",desk," cannot be opened")
    quit() #Termina la búsqueda y no permite su avance
    
count = 0
for search in abrir:
    search = search.rstrip()
    if search.startswith('ID de reunión'):
        count = count + 1
print('There were', count, 'results for your query in', desk)
