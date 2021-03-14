import os
import math
print("Print the bigger number by not using the reserved function max(). Declare a function (def) that execute the same logic")


def my_max(x,y):
    if (x < y):
        txt = "The bigger number is {}"
        print(txt.format(y))
    
    if (x > y):
        txt = "The bigger number is {}"
        print(txt.format(x))

arg1 = int(input("Introduce Number 1 --> "))
arg2 = int(input("Introduce number 2 --> "))

my_max(arg1,arg2)
