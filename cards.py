"""
This module contains playing card and deck classes
"""

import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.custom_value = 0

class Deck:
    # n is number of standard decks
    def __init__(self, n = 1):
        suits = ['diamonds', 'hearts', 'spades', 'clubs']
        faces = ['jack', 'queen', 'king', 'ace']
        # odeck is a deck with all the cards originally in it, unmodified
        self.odeck = [Card(i, j) for i in range(2, 11) for j in suits]
        self.odeck.extend([Card(i, j) for i in faces for j in suits])
        self.odeck = self.odeck * n
        # deck is the deck that the methods work with
        self.deck = list(self.odeck)

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count == len(self.deck):
            raise StopIteration
        self.count += 1
        return self.deck[self.count - 1]

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

    def add_cards(self, cards):
        self.deck.extend(cards)

    def remove(self, card):
        try:
            self.deck.remove(card)
        except ValueError:
            print("That card is not in the deck!")

    def cards_left(self):
        return len(self.deck)

    def refresh(self):
        """
        Makes the deck what it was initialized to be again
        """
        self.deck = list(self.odeck)

class GenDeck:
    def __init__(self, n = 1):
        suits = ['diamonds', 'hearts', 'spades', 'clubs']
        faces = ['jack', 'queen', 'king', 'ace']
        self.odeck = [Card(i, j) for i in range(2, 11) for j in suits]
        self.odeck.extend([Card(i, j) for i in faces for j in suits])
        self.odeck = self.odeck * n
        self.numcards = len(self.odeck)

        self.deck = (card for card in self.odeck)

        #d = ([Card(i, j)] * n for i in range(2, 11) for j in suits)
        #self.deck = itertools.chain.from_iterable(d)
        #d = ([Card(i, j)] * n for i in faces for j in suits)
        #self.deck = itertools.chain(self.deck, itertools.chain.from_iterable(d))

    def __iter__(self):
        return self

    def __next__(self):
        self.numcards -= 1
        return next(self.deck)

    def draw(self):
        try:
            return next(self.deck)
            self.numcards -= 1
        except StopIteration:
            print("Deck is empty!")

    def shuffle(self):
        d = list(self.deck)
        random.shuffle(d)
        self.deck = (card for card in d)

    def cards_left(self):
        return self.numcards

    def refresh(self):
        self.deck = (card for card in self.odeck)
        self.numcards = len(self.odeck)



