from HigerVsLower_game_art import logo, vs
from HigerVsLower_game_data import data
import random


def print_choices(dataA, dataB, vsArt):
  """ prints out the choices for the user to make  """""
  nameA = dataA["name"]
  desA = dataA["description"]
  couA = dataA["country"]

  nameB = dataB["name"]
  desB = dataB["description"]
  couB = dataB["country"]
  
  print(f"\nCompare A: {nameA}, a {desA}, from {couA}")
  print(vsArt)
  print(f"Against B: {nameB}, a {desB}, from {couB}\n")


def compare(dataA, dataB, input):
  """Compares the 2 dictionaries and returns the winner"""""
  dataA_score = dataA["follower_count"]
  dataB_score = dataB["follower_count"]
  
  if dataA_score > dataB_score:
    moreFollowers = 'a'
  elif dataA_score < dataB_score:
    moreFollowers = 'b'

  if(input == moreFollowers):
    return 1
  else:
    return -1


def game(data, logo, vs):
  print(logo)
  
  score = 0
  dataB = random.choice(data)
  game_is_on = True
  
  while(game_is_on):
    dataA = dataB
    dataB = random.choice(data)

    while (dataA == dataB):
      dataB = random.choice(data)

    print_choices(dataA, dataB, vs)
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    comp_result = compare(dataA, dataB, user_choice)

    if (comp_result == 1):
      score += 1
      print(f"\nYou're right! Current score: {score}.")
    else:
      print(f"\nSorry, that's wrong. Final score: {score}")
      game_is_on = False
    
  
game(data, logo, vs)

