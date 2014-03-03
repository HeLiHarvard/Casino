#! /usr/bin/env python3.3

"""
This program runs a basic blackjack game. Currently it is
just you versus the dealer.
"""
import cards

#Set custom values for face cards and ace
def set_custom_value(deck):
    d = list(deck)
    for card in d:
        if card.value in ['jack', 'queen', 'king']:
            card.custom_value = 10
        elif card.value == 'ace':
            card.custom_value = 11
        else:
            card.custom_value = card.value
    deck.deck = (card for card in d)

#Draws cards and evaluates aces
def play_hand(player_name, deck, player_hand, player_total):
    new_card = deck.draw()
    player_hand.append(new_card)
    print(player_name + " drew a " + str(new_card.value) + " of " + new_card.suit)
    player_total += new_card.custom_value

    if player_total > 21 and any(c.value == 'ace' for c in player_hand):
        for card in player_hand:
            if card.value == 'ace':
                card = cards.Card('1ace', card.suit, 1)
                break
        player_total -= 10
    return player_total

deck = cards.GenDeck()
deck.shuffle()
set_custom_value(deck)
deck_size = deck.cards_left()

print("Welcome to Blackjack!")
cash = float(input("How much cash are you playing with today? $"))
net_earnings = 0

proceed = "y"

#Main
while proceed != "n":
    # Shuffle when deck is more than 60% gone
    if (deck.cards_left() / deck_size) < .4:
        deck.refresh()
        deck.shuffle()
        set_custom_value(deck)
        print("Deck has been re-shuffled!")

    bet = float(input("Enter your bet for this round: $"))
    while cash - bet < 0:
        bet = float(input("Not enough cash. Please enter a smaller bet: $"))

    dealer_hand = [deck.draw(), deck.draw()]
    print("Dealer drew a " + str(dealer_hand[0].value) + " of " + dealer_hand[0].suit
           + " and placed a card facedown.")

    dealer_total = sum(card.custom_value for card in dealer_hand)

    your_hand = [deck.draw(), deck.draw()]
    print("You got a " + str(your_hand[0].value) + " of " + your_hand[0].suit, end = "")
    print(" and a " + str(your_hand[1].value) + " of " + your_hand[1].suit)

    your_total = sum(card.custom_value for card in your_hand)

    print("Your hand's point value is " + str(your_total))

    #If someone wins at the initial draw
    if dealer_total == 22:
        dealer_hand[0] = cards.Card('1ace', dealer_hand[0].suit, 1)
        dealer_total -= 10
    if dealer_total == 21:
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
    else:
        while your_total < 21:
            choice = input("Do you wish to [h]it or [s]tand? ")
            if choice[0].lower() == 's':
                break
            your_total = play_hand('You', deck, your_hand, your_total)
            print("Your hand's point value is " + str(your_total))
        if your_total > 21:
            print("You have busted! You lose this round.")
            print("You lost $" + str(bet))
            net_earnings -= bet
            cash -= bet
        else:
            while (dealer_total < 17 or
                  (dealer_total == 17 and any(c.value == 'ace' for c in dealer_hand))):
                dealer_total = play_hand('Dealer', deck, dealer_hand, dealer_total)
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


