import numberGuessingArt
import random

print(numberGuessingArt.logo)

def difficulty(diffInput):
    
    if (diffInput == "hard"):
        return 5
    elif (diffInput == "easy"):
        return 10
    else:
        return - 1
    
def guesses(attempts):
    print(f"you have {attempts} remaining to guess the number.")
                  
    
def scoring(randNumber, guess):
    
    
    if (guess < 1 or guess > 100):
        return -1
    
    if (guess > randNumber):
        return 0 
    elif(guess < randNumber):
        return 1
    elif(guess == randNumber):
        return 2
    
        
def numberGuessingGame():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    dificulty = difficulty(input("Choose a dificulty. Type 'easy' or 'hard': ").lower())
    
    while (dificulty == -1):
       dificulty =  difficulty(input("Choose a dificulty. Type 'easy' or 'hard': ").lower())
        
    randNum = random.randint(1, 100)
    
    while (dificulty != 0 ):
        guesses(dificulty)
        guess = input("Make a guess: ")
        scored = scoring(randNum, int(guess))
        
        if scored == -1 :
            print("Enter a valid number")
        elif scored == 0:
            print("Too high")
            print("guess again")
        elif scored == 1:
            print("Too low")
            print("guess again")
        elif scored == 2:
            print(f"You got it! The answer was {randNum}")
            break
        
        dificulty -= 1

numberGuessingGame()