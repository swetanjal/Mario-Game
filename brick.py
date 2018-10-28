"""This file contains implementation of brick class."""
from config import BRICK_HEIGHT, BRICK_WIDTH


class Brick:
    """This class implements brick object in game."""

    def __init__(self, x_coord, y_coord):
        """Constructor"""
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = BRICK_WIDTH
        self.height = BRICK_HEIGHT

    def get_x(self):
        """Returns X coordinate of brick"""
        return self.x_coord

    def get_y(self):
        """Returns Y coordinate of brick."""
        return self.y_coord
