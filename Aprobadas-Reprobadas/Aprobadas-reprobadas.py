
print ('Phyton - Calcular el promedio de notas')

notas = [8,3,7,9,10,5,6,9,10]
ap = 0
pro_ap = 0
suma_ap = 0
rep = 0
pro_rep = 0
suma_rep = 0

for x in notas:
    if x >=7:
        ap = ap + 1
        prop_ap = pro_ap + x
        suma_ap = pro_ap / ap
    else:
        rep = rep + 1
        pro_rep = pro_rep + x
        suma_rep = pro_rep / rep
        
print("El promedio de notas aprobadas fue de---> ", int(suma_ap))
print("El promedio de notas reprobadas fue de---> ", int(suma_rep))
