import random

rint = random.randint(1,2)
rflo = random.random()

print(
"""
Welcome to the Coin Guessing Game!
Choose a method to toss the coing:
1. using random.random()
2. using random.randint()         
""")

meth = input("Enter your choice (1 or 2): ")

while (meth != "1" and meth != "2"):
    meth = input("Enter your choice (1 or 2): ")

meth = int(meth)

if (meth == 1):
    if(rflo <= 0.5):
        computerChoice = "heads"
    else:
        computerChoice = "tails"

elif (meth == 2):
    if(rint == 1):
        computerChoice = "heads"
    else:
        computerChoice = "tails"
    
else:
    print("Invalid choice. Please select eiither 1 or 2.")


userChoice = input("Enter your guess (Heads or Tails): ").lower()

while (userChoice != "heads" and userChoice != "tails"):
    userChoice = input("Enter your guess (Heads or Tails): ").lower()


if (computerChoice == userChoice):
    print("Congratulations! You won!")
    print(f"The computer's toss result was: {computerChoice}")
else:
    print("Sorry! You lost!")
    print(f"The computer's toss result was: {computerChoice}")
    


