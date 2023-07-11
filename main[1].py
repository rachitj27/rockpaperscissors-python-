print("Rock Paper Scissors")
game  = True
import random
you_wins = 0
cpu_wins = 0
computer = ["rock", "paper", "scissors"]
while game:
  print("\nYou: " + str(you_wins))
  print("CPU: " + str(cpu_wins))
  player_choice = input("\nChoose Rock(r) Paper(p) or Scissors(s): ")
  computer_choice = random.choice(computer)
  print("CPU chose " + computer_choice)
  if player_choice == "p" and computer_choice == "rock":
     print("You Win")
     you_wins = you_wins + 1
  elif player_choice == "p" and computer_choice == "paper":
    print("You Tied")
  elif player_choice == "p" and computer_choice == "scissors":
    print("You Lose")
    cpu_wins = cpu_wins + 1
  if player_choice == "r" and computer_choice == "scissors":
     print("You Win")
     you_wins = you_wins + 1
  elif player_choice == "r" and computer_choice == "rock":
    print("You Tied")
  elif player_choice == "r" and computer_choice == "paper":
    print("You Lose")
    cpu_wins = cpu_wins + 1
  if player_choice == "s" and computer_choice == "paper":
     print("You Win")
     you_wins = you_wins + 1
  elif player_choice == "s" and computer_choice == "scissors":
    print("You Tied")
  elif player_choice == "s" and computer_choice == "rock":
    print("You Lose")
    cpu_wins = cpu_wins + 1
  else:
    print("Please choose rock paper or scissors")
