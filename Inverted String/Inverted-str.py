def invertir_cadena(chain):
    y = len(chain)
    x = -1
    z = ""
    for i in range(y,0,-1):
        z += chain[x]
        x = x - 1
    print(z)
    return z
  

cadena = input("Escribe una cosita y haré que se vea a la inversa --> ")
invertir_cadena(cadena)
        
