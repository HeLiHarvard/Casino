"""
This module provides a dice class providing for dice with
any number of sides, not just six
"""
import random

class Die:
    """
    A die whose values vary from 1 to however many is passed as
    an argument for the number of sides.
    """
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        """
        Rolls the die, returns a random value from 1 to the number of sides
        """
        return random.randrange(1, sides + 1)

    def change_sides(self, sides):
        """
        Changes how many sides the die has
        """
        self.sides = sides

class CustomDie:
    """
    A die whose sides' values are input by the user
    """

    def __init__(self, sides):
        """
        Takes an iterator argument to determine values on the die
        """
        self.sides = list(sides)

    def roll(self):
        """
        Randomly returns one of the values on the die
        """
        return random.choice(self.sides)

    def change_sides(self, sides):
        """
        Changes the number of sides and/or the sides' values
        """
        self.sides = list(sides)


