import random
from hangmanwords import word_list
from hangman_ARt import stages, logo

print(logo)
lives = 6
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)


correct_letters =[]
guessed_letters = []

is_game_over = False
while not is_game_over:
    guess = input("Make your guess: ").lower()
    display = ""
    if guess in guessed_letters:
        print("You have guessed this letter before! akal ni haigi! lock in")
    guessed_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            if guess in guessed_letters:
                print("You have guessed this letter before! akal ni haigi! lock in")
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if lives == 0:
        is_game_over = True
        print(chosen_word)
        print("you loose!")
    if "_" not in display:
        print("YAYAYAYAYA YOU WINNNN")

    print(stages[::-1][lives])
    print(display)
    print(f"You have {lives} left! Singh lock in appa khalistan banona")







# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#  e.g. You guessed d, that's not in the word. You lose a life.
