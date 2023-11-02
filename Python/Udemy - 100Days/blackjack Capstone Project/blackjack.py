############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
##
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
import blackjackArt
print(blackjackArt.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerCards = []
dealerCards = []


def playerCard(times, cards):
  tempPlayerCards = []
  for x in range(times):
    playerCardChoice = random.choice(cards)
    tempPlayerCards.append(playerCardChoice)
  return tempPlayerCards
  
def dealerCard(times, cards):
  tempDealerCards = []
  for x in range(times):
    dealerCardChoice = random.choice(cards)
    tempDealerCards.append(dealerCardChoice)
  return tempDealerCards

def scoreCalculator(cardsList):
  score = 0
  for item in cardsList:
    score += item
  return score

def finalMessage(playerCards, playerScore, dealerCards, dealerScore):
  print(f"Your final hand: {playerCards}, final score: {playerScore}")
  print(f"Computer's final hand: {dealerCards}, final score: {dealerScore}")

def finalScoring(playerScore, dealerScore,playerCards,dealerCards):
  if (playerScore == dealerScore):
    print ("it's a draw ")
  elif ( playerScore == 21 ):
    if (len(playerCards) == 2):
      if (11 in playerCards):
      # if(playerCards[0] == 11):
        print("Blackjack! You win!")
  elif ( dealerScore == 21 ):
    if (len(dealerCards) == 2):
      if(11 in dealerCards):
      # if(dealerCards[0] == 11):
        print("Computer got Blackjack! You Lose!")        

  
  if (playerScore > 21):
    print ("\nYou went over, you lose 😥")
  elif (dealerScore > 21):
    print ("\nOponent went over, you win 😄")
  elif (playerScore > dealerScore):
    print ("your score is higher, you win 😄")
  elif(playerScore < dealerScore):
    print ("Computer's score is higher, you lose 😥")
  

def game():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  playerCards = []
  dealerCards = []
  dealerCardsTimes = random.randint(1,4)

  
  playerCards.extend(playerCard(2, cards)) 
  playerScore = scoreCalculator(playerCards)
  print(f"Your Cards: {playerCards}, current score: {playerScore}")

  dealerCards.extend(dealerCard(1, cards))
  dealerScore = scoreCalculator(dealerCards)
  print(f"Computer's first card: {dealerCards[0]}\n")

  anotherCard = input("Type y to get another card, or type n to pass: ").lower()
  if anotherCard == "y":
    newLoop = True
  elif anotherCard == "n":
    newLoop = False

  while(newLoop):
    playerCards.extend(playerCard(1, cards))
    playerScore = scoreCalculator(playerCards)
    print(f"Your Cards: {playerCards}, current score: {playerScore}")
    print(f"Computer's first card: {dealerCards[0]}\n")

    if (playerScore > 21 ):
      # print("You went Over, you lose 😥")
      newLoop = False
      finalMessage(playerCards, playerScore, dealerCards, dealerScore)
      finalScoring(playerScore, dealerScore, playerCards, dealerCards )
      return
    else:
      anotherCard = input("Type y to get another card, or type n to pass: ").lower()
      if anotherCard == "y":
        newLoop = True
      elif anotherCard == "n":
        newLoop = False

  dealerCards.extend(dealerCard(1, cards))
  dealerScore = scoreCalculator(dealerCards)
  while(dealerScore < 17):
    dealerCards.extend(dealerCard(1, cards))
    dealerScore = scoreCalculator(dealerCards)


  finalMessage(playerCards, playerScore, dealerCards, dealerScore)
  finalScoring(playerScore, dealerScore, playerCards, dealerCards)



game()


while ( input("do you want to play again, y for yes or n for no: ") == 'y'):
  print(blackjackArt.logo)
  game()
