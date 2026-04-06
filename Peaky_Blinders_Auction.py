from platform import processor
from Blinders_Auction_logo_art import logo
print(logo)
def get_highest_bid(bids):
    highest_bid = 0
    winner =''
    for bid in bids:
        bid_amount = bids[bid]
        if bids[bid] > highest_bid:
            highest_bid = bids[bid]
            winner = bid
        print(f"The Highest Bid is {highest_bid} by {winner}")



list_of_bids = {}
is_game_on = True
print("highest bid wins!")


while is_game_on:
    name = input("What is your name?")
    bid = int(input("what is your bid?: $"))
    other_bids = input("Are there any other bids?: Type \"yes\" or \"no\"").lower()
    list_of_bids[name] = bid

    if other_bids == "no":
        is_game_on = False
        get_highest_bid(list_of_bids)
        print("list_of_bids")
    elif other_bids == "yes":
        print("\n" * 67)
    else:
        print("Please enter either Yes or NO! R U slow?")
print(list_of_bids)




# Functionality
# Each person writes their name and bid.
# The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
# Each person's name and bid are saved to a dictionary.
# Once all participants have placed their bid, the program works out who has the highest bid and prints it
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
