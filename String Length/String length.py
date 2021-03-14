print ('By not using the reserved function len(). Declare a function (def) that execute the same logic')

def longitud(adv):
    cont = 0
    for i in adv:
        cont +=1
    return cont
    '''acum the range from the for loop'''
string = input("Write a string --> ")

print(longitud(string))
