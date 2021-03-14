import math
import os

edad = 1

acum_kid = 0
acum_teen = 0
acum_adulto = 0
acum_amayor= 0
acum_bebe = 0

personas_acum = 0
suma_edad = 0
edad_promedio = 0

print ('**************Python Practice: IF Conditionals*********************')
print("Clasify people by their Ages")

while edad != 0:
        n = input("Introduce a person's age --> ")
        edad = int(n);
        
        if edad > 0:
            personas_acum = personas_acum + 1
            suma_edad = suma_edad + edad
            edad_promedio = suma_edad / personas_acum
        
        if edad >=1 and edad <=3:
            acum_bebe = acum_bebe + 1
            
        elif edad >=4 and edad <=12:
            acum_kid = acum_kid + 1
            
        elif edad >=13 and edad <=17:
            acum_teen = acum_teen + 1
        
        elif edad >=18 and edad <=64:
            acum_adulto = acum_adulto + 1
        
        elif edad >=65:
            acum_amayor = acum_amayor + 1

print("\n Ages Count: \n ")

print("Baby: ", acum_bebe)
print("Kid: ", acum_kid)
print("Teenager: ", acum_teen)
print("Adult: ", acum_adulto)
print("Elder Adult: ", acum_amayor)

print("People's Age Summary -> ", personas_acum)
print("Average Age Summary - > ", edad_promedio)
        
