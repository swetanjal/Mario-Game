"""This file contains class implementing Fire objects."""
class Fire:
    """This class contains the template for fire objects."""
    def __init__(self, x_coord, y_coord, speed):
        """Constructor."""
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.speed = speed

    def update(self, mario, board):
        """This method updates the location of fire every frame."""
        for i in range(3):
            for j in range(3):
                for k in range(2):
                    for l in range(2):
                        if mario.x_coord + i == self.x_coord + k \
                        and mario.y_coord + j == self.y_coord + l:
                            board.game_over = 1
                            return
        self.x_coord = self.x_coord + self.speed

    def pass_test(self):
        """Dummy function"""
        pass

    def __del__(self):
        """Destructor"""
        pass
