from config import *
from random import randint


class Pipe:
    def __init__(self, X, Y, WIDTH, HEIGHT):
        self.X = X
        self.Y = Y
        self.height = HEIGHT
        self.width = WIDTH
        self.cnt = 0
