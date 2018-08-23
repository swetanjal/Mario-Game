from person import *
from config import *
from fire import *
from random import randint


class Boss(Person):
    def __init__(self, X, Y, HEIGHT, WIDTH):
        Person.__init__(self, X, Y, HEIGHT, WIDTH)
        self.speed_X = -1
        self.speed_Y = -1
        self.iniX = X
        self.iniY = Y
        self.cnt = 0

    def update(self, mario):

        if abs(self.iniX - self.X) > 12:
            self.speed_X = -self.speed_X
        if self.iniY - self.Y < 0:
            self.speed_Y = -self.speed_Y
        if self.iniY - self.Y > 12:
            self.speed_Y = -self.speed_Y
        if mario.X > self.X and self.Y == self.iniY:
            self.speed_Y = 0
        self.X = self.X + self.speed_X
        self.Y = self.Y + self.speed_Y
        self.mod = 24

    def fire_fire(self, mario, board):
        if abs(mario.X - self.X) < 2 * BOARD_WIDTH and self.cnt % self.mod == 0:
            sp = 1
            self.mod = 48
            if mario.X < self.X:
                sp = -1
                if sp == 1:
                    self.mod = 24
            if mario.X - self.X > 0:
                sp = sp * 3
            xxx = self.X
            flag = 1
            for fire in board.fire:
                if abs(fire.X - xxx) <= 5:
                    flag = 0
            if flag == 1:
                board.fire.append(Fire(self.X, self.Y + randint(3, 6), sp))
        self.cnt = self.cnt + 1
