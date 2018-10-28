"""This file contains implementation of pole that marks end of level."""


class Pole:
    """This class contains implementation of Pole object."""

    def __init__(self, X, Y, height):
        """Constructor"""
        self.x_coord = X
        self.y_coord = Y
        self.height = height

    def get_x(self):
        """This function returns X coordinate of Pole."""
        return self.x_coord

    def get_y(self):
        """This function retuns Y coordinate of Pole."""
        return self.y_coord
