#! /usr/bin/env python3.3

"""
This program runs a basic blackjack game. Currently it is
just you versus the dealer
"""
# TBD: Shuffle at around 60% of the deck gone
#      Display cash remaining and net earnings so far
#      Dealer AI
#      Win/Loss conditions


import random
import cards

deck = cards.Deck(6)
deck.shuffle()

print("Welcome to Blackjack!")
cash = float(input("How much cash are you playing with today? $"))
net_earnings = 0

proceed = "y"

while proceed != "n":
    bet = float(input("Enter your bet for this round: $"))
    while cash - bet < 0:
        bet = float(input("Not enough cash. Please enter a smaller bet: $"))

    cash -= bet

    dealer_hand = [deck.draw(), deck.draw()]
    print("Dealer drew a " + str(dealer_hand[0].value) + " of " + dealer_hand[0].suit)
    print("Dealer also drew and placed a card facedown.")

    for card in dealer_hand:
        if card.value in ['jack', 'queen', 'king']:
            card.value = 10
        if card.value == 'ace':
            card.value = 11


    your_hand = [deck.draw(), deck.draw()]
    print("You got a " + str(your_hand[0].value) + " of " + your_hand[0].suit, end = "")
    print(" and a " + str(your_hand[1].value) + " of " + your_hand[1].suit)


    print("You have $" + cash + " left.")
    # also print net earnings, which are calculated depending on winning or losing
    proceed = input("Continue[y/n]? ")[0].lower()


