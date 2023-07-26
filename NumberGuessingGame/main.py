from random import randrange as R

def guess():
        pguess = input("Guess my number between 1-100: ")
        try:
            pguess = int(pguess)
            if pguess > x:
                print("To high")
                guess()    
            elif pguess < x:
                print("To small")
                guess() 
            elif pguess == x:
                print("Congrats, you guessed the right number")
        
        except:
            print("Error, not a number")
        
        
        
    
        
            
while True:            
    x = R(1,100)            
    guess()
