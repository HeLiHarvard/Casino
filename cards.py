"""
This module contains playing card and deck classes
"""

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Deck:

    # number is number of standard decks
    def __init__(self, number):
        suits = ['diamonds', 'hearts', 'spades', 'clubs']
        self.deck = [Card(i, j) for i in range(1, 14) for j in suits]
