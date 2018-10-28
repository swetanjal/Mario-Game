"""This file contains class implementing Mario character."""
from person import Person
from config import MARIO_HEIGHT, MARIO_WIDTH


class Mario(Person):
    """Class of Mario character which inherits from Person class"""

    def __init__(self, X, Y):
        """Constructor"""
        Person.__init__(self, X, Y, MARIO_HEIGHT, MARIO_WIDTH)

    def get_x(self):
        """This function returns X coordinate of Mario."""
        pass

    def get_y(self):
        """This function returns the Y coordinate of Mario"""
        pass
