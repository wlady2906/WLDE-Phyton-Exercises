print ('Phyton - Realizar un programa que permita ingresar numeros hasta que sea 0')

acum_neg = 0
for x in range(0,5):
    y=input("Ingrese un valor para empezar---> ")
    n=int(y)
    
    if n < 0:
        acum_neg = acum_neg + 1
        
print("La cantidad de negativos fue de--->", acum_neg)
