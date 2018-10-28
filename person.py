"""Class containing defintion of game characters like Mario, enemies, etc."""
from config import PIPE_SYMBOL


class Person:
    """Sets up the Person object"""
    gravity = [-4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, X, Y, HEIGHT, WIDTH):
        """Constructor"""
        self.x_coord = X
        self.y_coord = Y
        self.height = HEIGHT
        self.width = WIDTH
        self.jump_state = 0
        self.jump_idx = 0

    def update(self, move_x, move_y, l_thresh, board, mario):
        """# Changes the position of Person object"""
        if self.x_coord + move_x > l_thresh:
            #self.X = self.X + move_x
            for i in range(abs(move_x)):
                if move_x > 0 and (board.board[self.y_coord][self.x_coord + 3] != 'B'
                                   and board.board[self.y_coord + 1][self.x_coord + 3] != 'B'
                                   and board.board[self.y_coord + 2][self.x_coord + 3] != 'B'):
                    self.x_coord = self.x_coord + 1
                if (move_x < 0 and (board.board[self.y_coord][self.x_coord - 1] != 'B'
                                    and board.board[self.y_coord + 1][self.x_coord - 1] != 'B'
                                    and board.board[self.y_coord + 2][self.x_coord - 1] != 'B')):
                    self.x_coord = self.x_coord - 1
                board.invalid(mario)
            try:
                if (board.board[self.y_coord + 3][self.x_coord] == ' ' \
                    or board.board[self.y_coord + 3][self.x_coord] == 'E') and \
                    (board.board[self.y_coord + 3][self.x_coord + 2] == ' ' or
                     board.board[self.y_coord + 3][self.x_coord + 2] == 'E') \
                        and self.jump_state == 0:
                    self.jump_state = 1
                    self.jump_idx = 4
                    move_y = Person.gravity[self.jump_idx]
            except:

                flag = 1
                flag = flag + 1

        for i in range(abs(move_y)):
            try:
                if (board.board[self.y_coord + 3][self.x_coord] == 'B'
                        or board.board[self.y_coord + 3][self.x_coord] == PIPE_SYMBOL
                        or board.board[self.y_coord + 3][self.x_coord + 1] == 'B'
                        or board.board[self.y_coord + 3][self.x_coord + 1] == PIPE_SYMBOL
                        or board.board[self.y_coord + 3][self.x_coord + 2] == 'B'
                        or board.board[self.y_coord + 3][self.x_coord + 2] == PIPE_SYMBOL) \
                        and Person.gravity[self.jump_idx] >= 0:
                    self.jump_idx = 0
                    self.jump_state = 0
                    return
                if move_y < 0:
                    self.y_coord = self.y_coord - 1
                else:
                    self.y_coord = self.y_coord + 1
                board.check_collision(self)
                # board.draw_mario()
                board.invalid(mario)

            except:
                flag = 1
                flag = flag + 1

        if self.jump_state == 1:
            self.jump_idx = self.jump_idx + 1
        if self.jump_idx >= len(Person.gravity):
            self.jump_idx = 0
            self.jump_state = 0

    def get_x(self):
        """Returns X coordinate of Person.."""
        return self.x_coord
    def get_y(self):
        """Return y coordinate of Person"""
        return self.y_coord
