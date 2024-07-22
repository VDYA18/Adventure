import random


def guessing_game():
    
    print("welcome to the number guessing game")
    print("i am thinking number between 1 to 100")
    
    secret_number=random.randint(1,100)
    attempt=0
    max_attempt=5
    
    while attempt<max_attempt:
        guess=(int(input("guess any number between 1 to 100 : ")))
        attempt+=1 
        
        if guess < secret_number:
            print("too low!")
            
        elif guess > secret_number:
            print("too high!")
            
        else:
            print("yay! you guess right number")
            exit()
            
    print("In this 5 attempts you didn't guessing a right number, the right answer is: ",secret_number) 
    print("better luck next time")
    

  


 


