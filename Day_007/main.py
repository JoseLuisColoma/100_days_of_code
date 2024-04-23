import random
from hangman_art import logo
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(logo)
print("\nBIENVENIDO AL JUEGO DEL AHORCADO\n")

display = []
for _ in range(word_length):
    display += "_"

print("La palabra tiene " + str(word_length) + " letras.\n")

print(f"{' '.join(display)}\n")

while not end_of_game:
    guess = input("Elige una letra: ").lower()
    if guess in display:
        print(f"Ya has elegido \"{guess}\"")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Has elegido la letra \"{guess}\", que no está en la palabra oculta.\nPierdes una vida.\n")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("LO SIENTO. HAS PERDIDO.\n")
            print(f"La palabra oculta era " + "\"" + chosen_word.upper() + "\"\n")

    print(f"{' '.join(display)}")

    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("\nENHORABUENA. HAS GANADO!!!!!!!!!!!.\n")
        print(f"La palabra oculta era " + "\n" + chosen_word.upper() + "\"\n")
