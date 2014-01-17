"""
This module contains playing card and deck classes
"""

import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Deck:
    # n is number of standard decks
    def __init__(self, n):
        suits = ['diamonds', 'hearts', 'spades', 'clubs']
        # odeck is a deck with all the cards originally in it, unmodified
        self.odeck = [Card(i, j) for i in range(1, 14) for j in suits] * n
        # deck is the deck that the methods work with
        self.deck = list(self.odeck)

    def __iter__(self):
        return self.deck

    def shuffle(self):
        random.shuffle(self.deck)

    def filter(self, func):
        self.deck = [c for c in self.deck if func(c)]

    def draw(self):
        if self.deck:
            return self.deck.pop(0)
        else:
            print("Deck is empty!")

    def pick_random(self):
        return self.deck.pop(random.randrange(len(self.deck)))

    def refresh(self):
        """
        Makes the deck what it was initialized to be again
        """
        self.deck = list(self.odeck)


