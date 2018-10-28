"""This file contains implementation of coin class."""
from random import randint


class Coin:
    """Template for coin object in the game."""

    def __init__(self, x_coord, y_coord):
        """Constructor"""
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.points = randint(5, 15)

    def get_x(self):
        """Returns the X coordinate of coin"""
        return self.x_coord

    def get_y(self):
        """Returns the Y coordinate of coin"""
        return self.y_coord
