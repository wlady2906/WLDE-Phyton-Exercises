print ('Devuelve las palabras que tengan más de N caracteres')

def filtrar_palabras(caracteres):
    #definimos una lista con palabras
    lista = ['Art Attack','Meliodas','Xavier','Busqueda','python','Algoritmo RS','lenguaje','alto']
    #variable para almacenar la longitud de dichas palabras
    n = int(caracteres)
    count = 0
    result = []
    for x in range(len(lista)):
        if len(lista[x]) == n:
            count = count + 1
            result = lista[x]
            print(lista[x])
    return count
    
        
caracteres = input('Busqueda de palabras por filtro(Introduce un numero) ')
print('Las palabras con la longitud dada son ',filtrar_palabras(caracteres))
