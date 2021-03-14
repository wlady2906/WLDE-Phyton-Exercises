print ('Imprime la palabra más larga contenida en una lista')

def mas_larga(lista):
    largo = '' #Dicha variable contendra una cadena vacia
    for i in range(len(lista)):
        if len(lista[i]) >= len(largo): #Evaluamos que la longitud de ambas cadenas sea mayor o igual que la otra
            largo = lista[i] #almacenamos al palabra en la variable largo
    return largo

#Declaramos un alista con los elementos en formato string  
lista = ['otorrinolaringologo','largo','alto','ancho','computadora','imposible','plausible']

print('la palabra mas larga es ', mas_larga(lista))
