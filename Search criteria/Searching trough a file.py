print ('Usar un criterio de busqueda para todas las lineas')
archivo = open("ZOOM ID.txt")

for search in archivo:
    search = search.rstrip()
    if not 'AGUIRRE MUNIZAGA' in search:
        continue
    print(search)
