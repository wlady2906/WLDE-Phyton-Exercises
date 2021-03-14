print ('Cada linea del archivo en mayusculas')
archivo = open("ZOOM ID.txt", "r")
count = 0

for search in archivo:
    search = search.rstrip()
    search = search.upper()#Convierte todas las letras del Texto en mayusculas
    print(search.strip())
    count = count + 1
    
print(count, "Lineas")
