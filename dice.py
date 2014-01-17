"""
This module provides a dice class providing for dice with
any number of sides, not just six
"""
import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randrange(1, sides + 1)

    def change_sides(self, sides):
        self.sides = sides

class CustomDie:
    def __init__(self, sides):
        self.sides = [input("Enter a side number: ") for i in range(sides)]

    def roll(self):
        return random.choice(self.sides)

    def change_sides(self, sides):
        print("Changing to a die with " + sides + " sides.")
        self.sides = [input("Enter a side number: ") for i in range(sides)]


