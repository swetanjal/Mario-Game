from person import *
from config import *

# Class of Mario character which inherits from Person class


class Mario(Person):
    def __init__(self, X, Y):
        Person.__init__(self, X, Y, MARIO_HEIGHT, MARIO_WIDTH)
