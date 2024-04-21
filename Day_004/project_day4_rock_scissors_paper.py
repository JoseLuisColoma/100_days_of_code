import random
import sys
from PIL import Image

GAME_PER_PLAY = "5"

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

user_score = 0
computer_score = 0

game_images = [rock, paper, scissors]

print("Welcome to \"Rock, Paper, Scissors\" Game")
print(f"This game is Best of {GAME_PER_PLAY}")

while user_score != 3 or computer_score != 3:
    print("What do you choose?")
    user_choice = int(input("0: Rock, 1: Paper, 2: Scissors\n"))

    if user_choice >= 3 or user_choice < 0:
        print("You typed and invalid number, the game is over!")
        sys.exit()

    print(f"You chose:")

    # Load user's choice image
    user_image_path = f"./images/{user_choice}.png"
    user_image = Image.open(user_image_path)
    user_image.show()

    print(f"Computer chose:")

    # Load computer's choice image
    computer_choice = random.randint(0, 2)
    computer_image_path = f"./images/{computer_choice}.png"
    computer_image = Image.open(computer_image_path)
    computer_image.show()
    print(game_images[user_choice])

    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!\n")
        user_score += 1
    elif computer_choice > user_choice:
        print("You lose!\n")
        computer_score += 1
    elif computer_choice == user_choice:
        print("It's a draw!\n")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!\n")
        computer_score += 1
    elif user_choice > computer_choice:
        print("You win!\n")
        user_score += 1

    print("--- SCORE ---")
    print(f"USER:     {user_score}")
    print(f"COMPUTER: {computer_score}")
    print("-------------")

    if user_score == 3:
        print(f"\nYou have won the game. Congratulations!!".upper())
        exit()
    if computer_score == 3:
        print(f"\nComputer has won the game. Next Time!!".upper())
        exit()