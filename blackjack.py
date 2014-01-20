#! /usr/bin/env python3.3

"""
This program runs a basic blackjack game. Currently it is
just you versus the dealer.
"""

#CHECK DEALER HAND'S LOGIC AS WELL

# Ideas for expansion:
# MAKE A GENERATOR DECK!!!!!!******
# Multiple players
# Let player choose number of decks
# Let player control action line by line? e.g. dealer draws, continue
# Double down
# Split
# Surrender (some games do this)
# Insurance (I've never heard, but apparently it's a thing)
# Card counter for strategic help?

import cards

def set_custom_value(deck):
    d = list(deck)
    for card in d:
        if card.value in ['jack', 'queen', 'king']:
            card.custom_value = 10
        elif card.value == 'ace':
            card.custom_value = 11
        else:
            card.custom_value = card.value
    # Idea: make GenDeck have a method constructing a deck from a list
    deck.deck = (card for card in d)

deck = cards.GenDeck(6)
deck.shuffle()
set_custom_value(deck)
deck_size = deck.cards_left()

print("Welcome to Blackjack!")
cash = float(input("How much cash are you playing with today? $"))
net_earnings = 0

proceed = "y"

while proceed != "n":
    # Shuffle when deck is more than 60% gone
    if (deck.cards_left() / deck_size) < .4:
        deck.shuffle()
        print("Deck has been re-shuffled!")

    bet = float(input("Enter your bet for this round: $"))
    while cash - bet < 0:
        bet = float(input("Not enough cash. Please enter a smaller bet: $"))

    dealer_hand = [deck.draw(), deck.draw()]
    print("Dealer drew a " + str(dealer_hand[0].value) + " of " + dealer_hand[0].suit)
    print("Dealer also drew and placed a card facedown.")

    dealer_total = sum(card.custom_value for card in dealer_hand)

    your_hand = [deck.draw(), deck.draw()]
    print("You got a " + str(your_hand[0].value) + " of " + your_hand[0].suit, end = "")
    print(" and a " + str(your_hand[1].value) + " of " + your_hand[1].suit)

    your_total = sum(card.custom_value for card in your_hand)

    print("Your hand's point value is " + str(your_total))

    if dealer_total == 22:
        dealer_hand[0].custom_value = 1
        dealer_total = sum(card.custom_value for card in dealer_hand)
    elif dealer_total == 21:
        if your_total == 21:
            print("You both got blackjacks! The result is a push.")
            print("No money won or lost.")
        else:
            print("The dealer got a blackjack! You lose this round.")
            print("You lost $" + str(bet))
            net_earnings -= bet
            cash -= bet
    elif your_total == 21:
        print("You got a blackjack and the dealer did not! You win this round.")
        print("You won $" + str(bet))
        net_earnings += bet
        cash += bet

    while your_total < 21:
        choice = input("Do you wish to [h]it or [s]tand? ")
        if choice[0].lower() == 's':
            break
        new_card = deck.draw()
        your_hand.append(new_card)
        print("You drew a " + str(new_card.value) + " of " + new_card.suit)
        your_total += new_card.custom_value

        if your_total > 21 and any(c.value == 'ace' for c in your_hand):
            for card in your_hand:
                if card.value == 'ace':
                    card.value = '1ace'
                    break
            your_total -= 10
        print("Your hand's point value is " + str(your_total))

    if your_total > 21:
        print("You have busted! You lose this round.")
        print("You lost $" + str(bet))
        net_earnings -= bet
        cash -= bet
    else:
        while (dealer_total < 17 or
              (dealer_total == 17 and any(c.value == 'ace' for c in dealer_hand))):
            d_card = deck.draw()
            dealer_hand.append(d_card)
            dealer_total += d_card.custom_value
            print("Dealer drew a " + str(d_card.value) + " of " + d_card.suit)
            if dealer_total > 21 and any(c.value == 'ace' for c in dealer_hand):
                for card in dealer_hand:
                    if card.value == 'ace':
                        card.value = '1ace'
                        break
                dealer_total -= 10

        print("The dealer's hand's point value is " + str(dealer_total))

        if dealer_total > 21:
            print("The dealer busted! You win this round.")
            print("You won $" + str(bet))
            net_earnings += bet
            cash += bet
        else:
            if your_total > dealer_total:
                print("Your total is closer to 21! You win this round.")
                print("You won $" + str(bet))
                net_earnings += bet
                cash += bet
            elif your_total < dealer_total:
                print("The dealer's total is closer to 21! You lose this round.")
                print("You lost $" + str(bet))
                net_earnings -= bet
                cash -= bet
            else:
                print("You and the dealer tied!")
                print("No money won or lost this round.")

    print("You have $" + str(cash) + " left.")
    print("Your net earnings are $" + str(net_earnings))
    proceed = input("Continue[y/n]? ")[0].lower()


