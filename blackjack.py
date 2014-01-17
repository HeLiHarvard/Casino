#! /usr/bin/env python3.3

"""
This program runs a basic blackjack game. Currently it is
just you versus the dealer
"""

import random
import cards

deck = cards.Deck(6)
dealer_hand = []
your_hand = []

print("Welcome to Blackjack!")
cash = int(input("How much cash are you playing with today? $"))
net_earnings = 0

proceed = "y"

while proceed != "n":

    proceed = input("Continue[y/n]? ").pop(0).lower()

