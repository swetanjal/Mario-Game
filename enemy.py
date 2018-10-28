"""This file contains class implementing the enemy objects."""
from person import Person
from config import ENEMY_HEIGHT, ENEMY_WIDTH, PIPE_SYMBOL



class Enemy(Person):
    """This class contains template for each enemy object."""
    def __init__(self, X, Y, speed=-1):
        """Constructor"""
        Person.__init__(self, X, Y, ENEMY_HEIGHT, ENEMY_WIDTH)
        self.speed = speed
        self.cnt = -1

    def move(self, l_thresh, board, mario):
        """This function controls the movement of enemy and updates it's position."""
        if (board.board[self.y_coord][self.x_coord + self.speed] == PIPE_SYMBOL or board.board[self.y_coord][self.x_coord + self.width + self.speed] == PIPE_SYMBOL):
            self.speed = -self.speed
        if self.speed >= 1:
            if board.board[self.y_coord + self.height][self.x_coord + self.width + 1] == ' ':
                self.speed = -self.speed
        if self.speed <= -1:
            if board.board[self.y_coord + self.height][self.x_coord - 1] == ' ':
                self.speed = -self.speed
        self.update(self.speed, 0, l_thresh, board, mario)
