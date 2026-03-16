import random
word_list = ["aurangzeb", "modi", "indra gandhi", "wazir khan", "abdali"]


chosen_word = random.choice(word_list)
placeholder = ""
display = ""
guess = input("Make your guess: ").lower()

for letter in chosen_word:
    placeholder += "_"
    if letter == guess:
        display += letter
    else:
       display += "_"
print(placeholder)
print(display)

# TODO-1: - Use a while loop to let the user guess again.
# TODO-2: Change the for loop so that you keep the previous correct letters in display.


