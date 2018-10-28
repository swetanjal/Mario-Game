'''This is the code for implementation of Boss class.'''
from random import randint
from config import BOARD_WIDTH
from person import Person
from fire import Fire


class Boss(Person):
    '''This is the implementation of Boss class.'''
    def __init__(self, X, Y, HEIGHT, WIDTH):
        '''Constructor'''
        Person.__init__(self, X, Y, HEIGHT, WIDTH)
        self.speed_x = -1
        self.speed_y = -1
        self.inix = X
        self.iniy = Y
        self.cnt = 0
        self.mod = 0

    def update(self, mario):
        '''Function to update position of Boss.'''
        if abs(self.inix - self.x_coord) > 12:
            self.speed_x = -self.speed_x
        if self.iniy - self.y_coord < 0:
            self.speed_y = -self.speed_y
        if self.iniy - self.y_coord > 12:
            self.speed_y = -self.speed_y
        if mario.x_coord > self.x_coord and self.y_coord == self.iniy:
            self.speed_y = 0
        self.x_coord = self.x_coord + self.speed_x
        self.y_coord = self.y_coord + self.speed_y
        self.mod = 24

    def fire_fire(self, mario, board):
        '''Function implementing firing by boss.'''
        if abs(mario.x_coord - self.x_coord) < 2 * BOARD_WIDTH and self.cnt % self.mod == 0:
            s_p = 1
            self.mod = 48
            if mario.x_coord < self.x_coord:
                s_p = -1
                if s_p == 1:
                    self.mod = 24
            if mario.x_coord - self.x_coord > 0:
                s_p = s_p * 3
            xxx = self.x_coord
            flag = 1
            for fire in board.fire:
                if abs(fire.x_coord - xxx) <= 5:
                    flag = 0
            if flag == 1:
                board.fire.append(Fire(self.x_coord, self.y_coord + randint(3, 6), s_p))
        self.cnt = self.cnt + 1
