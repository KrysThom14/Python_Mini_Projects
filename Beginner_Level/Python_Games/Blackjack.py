# House Rules:
# 1.) The deck is unlimited in size.
# 2.) There are no jokers.
# 3.) The Jack/Queen/King all count as 10.
# 4.) The the Ace can count as 11 or 1.
# 5.) Use the following list as the deck of cards:
# 6.) cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# 7.) The cards in the list have equal probability of being drawn.
# 8.) Cards are not removed from the deck as they are drawn.
# 9.) The computer is the dealer.

import random
import os

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

def play_game():

    print(logo)

    player_cards = []
    dealer_cards = []
    keep_playing = True

    # This will pick 2 random cards for the player and dealer at the start of game
    for i in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while keep_playing:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"         Your cards: {player_cards}; Current Score = {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            keep_playing = False
        else:
            player_hits = input("Type 'y' to Hit or 'n' to Pass: ")
            if player_hits == "y":
                player_cards.append(deal_card())
            else:
                keep_playing = False

        print('') # Add an extra space/gap in console between card deals

    # Dealer will continue picking cards until dealer has >= 17 or Blackjack
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"   Your final hand: {player_cards}; Final Score = {player_score}")
    print(f"Dealer's final hand: {dealer_cards}; Final Score = {dealer_score}")
    print(compare_hands(player_score, dealer_score))

def deal_card():
    # This will pick a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # This will assign a 'Blackjack' a score of 0
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # This will change an ace from '11' to '1' if over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_hands(player_score, dealer_score):
    # This will determine a winner
    if player_score == dealer_score:
        return "*****It's A Draw!*****"
    elif dealer_score == 0:
        return "*****Sorry, You Lose. The Dealer Has A Blackjack*****"
    elif player_score == 0:
        return "*****You Win With A Blackjack!*****"
    elif player_score > 21:
        return "*****Sorry, You Lose. You Went Over.*****"
    elif dealer_score > 21:
        return "*****You Win! The Dealer Went Over.*****"
    elif player_score > dealer_score:
        return "*****You Win!*****"
    else:
        return "*****Sorry, You Lose.*****"

# This will be called when the console needs to be cleared at the start of a new game
def clear_console():
    os.system('cls')

# This will determine whether to start a new game or end program
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear_console()
    play_game()
