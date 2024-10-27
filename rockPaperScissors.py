import random

def get_choices():
  player_choice = input ("Enter a choice (rock, paper, scissors): ")
  computer_choice = random.choice (["rock", "paper", "scissors"])
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win (player, computer):
  print (f"You chose {player}, computer chose {computer}")
  if player == computer:
    print ("it's a tie!")

values = get_choices()
check_win(values)