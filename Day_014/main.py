import random
from art import *
from game_data import data


def clear():
    print("\n" * 100)


def get_player():
    account = random.choice(data)
    account_name = account['name']
    account_follower_count = account['follower_count']
    account_description = account['description']
    account_country = account['country']
    compare = f'{account_name}, a {account_description}, from {account_country}'
    return compare, account_follower_count


def game():
    clear()
    print(logo)
    score = 0
    isCorrect = True
    player_a, followers_a = get_player()

    while isCorrect:
        player_b, followers_b = get_player()

        # Asegurarse de que player_b no sea igual a player_a
        while player_b == player_a:
            player_b, followers_b = get_player()

        print(f"Compare A: {player_a}")
        print(vs)
        print(f"Against B: {player_b}")

        answer = input("\nWho do you think has more followers? Type 'a', or 'b': ").upper()

        if (answer == 'A' and followers_a > followers_b) or (answer == 'B' and followers_b > followers_a):
            score += 1
            print(f"Correct! Your current score is: {score}.")
        else:
            print(f"\nIncorrect, your final score is {score}.")
            isCorrect = False

        # Ahora, actualizar player_a y followers_a con los valores de player_b y followers_b
        player_a, followers_a = player_b, followers_b

    play_again = input("\nDo you want to play again? Type 'Y' or 'N': ").upper()
    if play_again == 'Y':
        game()
    elif play_again == 'N':
        print("Thanks for playing!")
        print("Goodbye.")


game()
