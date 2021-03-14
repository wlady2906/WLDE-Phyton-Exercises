''''
El asterisco(*) en un argumento indica que puedo almacenar varios datos en una lista
al usarla como parte de una función
''''
def suma(*lista):
    y = 0
    for i in lista:
        y += i
        txt = "La suma de la lista da como resultado: {}"
    print(txt.format(y))
    return y
    
''' Recordar que se inicia en 1 cuando es multiplicación '''    
def multi(*lista):
    x = 1  
    for i in lista:
        x *= i
    txt = "La multiplicación de la lista da como resultado: {}"
    print(txt.format(x))
    return x
    

n1 = int(input("Primer Número --> "))
n2 = int(input("Segundo Número --> "))
n3 = int(input("Tercer Número ---> "))


suma(n1,n2,n3)
multi(n1,n2,n3)
