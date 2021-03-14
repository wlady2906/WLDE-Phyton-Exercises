import os
import math

def inversa(char):
    y = len(char)
    z = ""
    b = -1
    
    for j in range(y,0,-1):
        z += char[b]
        b = b - 1
        
    print(z)
    return z

def es_palindromo(cadena):
    k = cadena
    w  = len(cadena)
    h = inversa(cadena)
    c = 0
    d = 0
    for i in range(w):
        if h[c] == k[c]:
            c += 1
            d +=  1
        else:
           print("No es palindromo")
           break
    
    if d == len(cadena):
        print("Es palindromo")
        
        
cadena = input("Escribe una cadena ---> ")
inversa(cadena)
es_palindromo(cadena)
