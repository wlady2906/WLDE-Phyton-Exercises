import os 
print ('Requesting Odd Numbers form keyboard')


imp = 0
while(imp != 5):
    x = input("Introduce a truly Odd number ---> ")
    n =int(x)
    
    if(n % 2 == 0):
        print("This number is not Odd. Try again")
        os.system("clear")
    else:
        imp = imp + 1
