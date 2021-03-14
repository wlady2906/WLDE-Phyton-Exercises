import random
import time 

#Definimos una función de introduccion para la presentacion del juego
def Introduccion():
    print('Estamos en una tierra mágica,llena de dragones. Delante nuestro')
    print('Se divisan dos cuevas. En una cueva, el dragon es amigable')
    print('Y compartira el tesoro contigo...')
    print('Sin embargo el otro dragon es codicioso, egoista y hambrienta. Te comerá apenas te vea....')
    print('Tu decides en que cuevas has de entrar....')
    print('')

#Funcion para elegir en que cueva entrar
def CambiarCueva():
    cueva = "" #variable cueva de tipo string vacio para almacenar la selección
    while cueva != "1" and cueva != "2":
        print('¿En que cueva decides entrar (1) o (2)? ')
        cueva = input()
        
    return cueva #retorno el resultado de la seleccion sea 1 o 2
    
    
#Función para evaluar la cueva a la que he ingresado, usamos el valor retornado en Cambiar Cueva
def checkCueva(CambiarCueva):
    print('Te acercas a la cueva...')
    time.sleep(2) #genera un delay hasta que aparezaca el proximo mensaje
    print('Está Oscuro y tenebroso...')
    time.sleep(2)
    print('Un gran dragon salta delante tuyo abre su boca y...')
    print('')
    time.sleep(2)
    
    #Variable cueva amigable, almacena numero aleatorio entre 1 y 2
    FriendlyCave = random.randint(1,2)
    
    if CambiarCueva == str(FriendlyCave):
        print('El dragon te ha entregado el tesoro')
    else:
        print('Has sido Devorado...Fin del juego')

EmpezarNuevo = 'SI'

while EmpezarNuevo == 'S' or EmpezarNuevo == 'Si' or EmpezarNuevo == 'SI':
    Introduccion()#LLamamos a la Introduccion
    NumCaverna = CambiarCueva()
    checkCueva(NumCaverna)
    
    print('¿Quieres jugar de nuevo? (Sí) o (No) ')
    EmpezarNuevo = input()
