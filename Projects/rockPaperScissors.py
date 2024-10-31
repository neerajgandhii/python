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
  elif player == "rock" and computer == "scissors":
    print("Rock smashes scissors! You win")
  elif player == "scissors" and computer == "paper":
    print("Scissors cut paper! You win")
  elif player == "paper" and computer == "rock":
    print("Paper covers rock! You win")
  elif player == "rock" and computer == "paper":
    print("Paper covers rock! You lose")
  elif player == "rock" and computer == "scissors":
    print("Rock smashes scissors! You win")

values = get_choices()
check_win(values)