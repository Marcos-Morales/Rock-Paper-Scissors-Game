import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#Take images above and place them into a list
game_images = [rock, paper, scissors]

#Ask the player what they would like to pick
player = int(input("What will you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

#Check and see if the player input is outside of the specified range
if player >= 3 or player < 0:
  print("You typed an invalid number, you lose!")
else:  
  print(game_images[player])

  #Allows the computer to pick a random number between 0, 1, and 2
  computer = random.randint(0, 2)
  
  print("Computer chose:")
  print(game_images[computer])

  #Defining the rules of the game
  if player == 0 and computer == 2:
    print("You win!")
  elif computer == 0 and player == 2:
    print("You lose!")
  elif computer > player:
    print("You lose")
  elif player > computer:
    print("You win!")
  elif computer == player:
    print("It's a draw!")