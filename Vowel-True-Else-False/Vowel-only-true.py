print ('Write a function (def) to compute True when a character is a vowel or False when it is not')

def vocal_true(x):
    if x == "a" or x == "e" or x=="i" or x=="o" or x=="u":
        txt = "It is a vowel"
        print (txt)
        return True
    
    if x == "A" or x == "E" or x=="I" or x=="O" or x=="U":
        txt = "It is a vowel"
        print (txt)
        return True
        
    else:
        txt = "It is not a Vowel"
        print (txt)
        return False

vocal = input("Write a letter and will tell you if is a vowel or not---> ")
vocal_true(vocal)
