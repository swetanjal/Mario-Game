from random import randint


class Coin:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.points = randint(5, 15)
