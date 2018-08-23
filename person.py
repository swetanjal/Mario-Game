# Class containing defintion of game characters like Mario, enemies, etc.
from config import *


class Person:
    # Sets up the Person object
    gravity = [-4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, X, Y, HEIGHT, WIDTH):
        self.X = X
        self.Y = Y
        self.height = HEIGHT
        self.width = WIDTH
        self.jump_state = 0
        self.jump_idx = 0
    # Changes the position of Person object

    def update(self, move_x, move_y, l_thresh, board, mario):
        if self.X + move_x > l_thresh:
            #self.X = self.X + move_x
            for i in range(abs(move_x)):
                if move_x > 0 and (board.board[self.Y][self.X + 3] != 'B' and board.board[self.Y + 1][self.X + 3] != 'B' and board.board[self.Y + 2][self.X + 3] != 'B'):
                    self.X = self.X + 1
                if (move_x < 0 and (board.board[self.Y][self.X - 1] != 'B' and board.board[self.Y + 1][self.X - 1] != 'B' and board.board[self.Y + 2][self.X - 1] != 'B')):
                    self.X = self.X - 1
                board.invalid(mario)
            try:
                if (board.board[self.Y + 3][self.X] == ' ' or board.board[self.Y + 3][self.X] == 'E') and (board.board[self.Y + 3][self.X + 2] == ' ' or board.board[self.Y + 3][self.X + 2] == 'E') and self.jump_state == 0:
                    self.jump_state = 1
                    self.jump_idx = 4
                    move_y = Person.gravity[self.jump_idx]
            except:
                pass

        for i in range(abs(move_y)):
            try:
                if (board.board[self.Y + 3][self.X] == 'B' or board.board[self.Y + 3][self.X] == PIPE_SYMBOL or board.board[self.Y + 3][self.X + 1] == 'B' or board.board[self.Y + 3][self.X + 1] == PIPE_SYMBOL or board.board[self.Y + 3][self.X + 2] == 'B' or board.board[self.Y + 3][self.X + 2] == PIPE_SYMBOL) and Person.gravity[self.jump_idx] >= 0:
                    self.jump_idx = 0
                    self.jump_state = 0
                    return
                if move_y < 0:
                    self.Y = self.Y - 1
                else:
                    self.Y = self.Y + 1
                board.check_collision(self)
                # board.draw_mario()
                board.invalid(mario)

            except:
                flag = 1
                # print("Idx")
        if self.jump_state == 1:
            self.jump_idx = self.jump_idx + 1
        if self.jump_idx >= len(Person.gravity):
            self.jump_idx = 0
            self.jump_state = 0
