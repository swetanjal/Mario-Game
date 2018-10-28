"""This file contains class implementing pipe objects in game."""


class Pipe:
    """This class implements pipe object in the game."""

    def __init__(self, X, Y, WIDTH, HEIGHT):
        """Constructor."""
        self.x_coord = X
        self.y_coord = Y
        self.height = HEIGHT
        self.width = WIDTH
        self.cnt = 0

    def get_x(self):
        """Returns X coordinate of Pipe"""
        return self.x_coord

    def get_y(self):
        """Retuns Y coordinate of Pipe."""
        return self.y_coord
