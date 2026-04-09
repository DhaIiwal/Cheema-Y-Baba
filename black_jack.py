# Normal 😎: Use all Hints below to complete the project.
# Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Expert 🤯: Only use Hint 1 to complete the project.
# Our Blackjack Game House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
import random

from Peaky_Blinders_Auction import is_game_on
from black_jack_art import logo
print(logo)

def  deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []

computer_cards = []
for x in range(0,2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards > 21):
        cards.remove(11)
        cards.append(1)
        return sum(cards)

    return sum(cards)

def compare_scores(user_cards, computer_cards):
    if sum(user_cards) == sum(computer_cards):
        return "Draw!"
    elif sum(user_cards) > sum(computer_cards):
        return "You win!"
    elif sum(user_cards) < sum(computer_cards):
        return "You Loose"
    elif sum(user_cards) > 21:
        return "You loose"
    elif sum(computer_cards) > 21:
        return "You Win"
    elif sum(user_cards) > 21 and sum(computer_cards) > 21:
        return "Draw! Go Again"
    return None
deal_cards()
def play_game():
    print (logo)
    user_cards[]
    computer_cards[]
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in Range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = computer_score(computer_cards)
        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Ty")
            if

while input("do you want to play a game of black Jack? Type'y' or 'n' ") == "y":
    play_game()
