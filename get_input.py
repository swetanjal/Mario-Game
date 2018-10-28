"""This file handles input from user."""
from sys import stdin
from termios import tcgetattr, ICANON, ECHO, tcsetattr, TCSAFLUSH, tcflush
from termios import TCIFLUSH, TCSANOW
from select import select


class Input:

    """This class handles input."""
    def __init__(self):
        """Constructor"""
        self.__fd = stdin.fileno()
        self.__new = tcgetattr(self.__fd)
        self.__old = tcgetattr(self.__fd)
        self.__new[3] = (self.__new[3] & ~ICANON & ~ECHO)
        tcsetattr(self.__fd, TCSAFLUSH, self.__new)

    def check_stream(self):
        """checkStream method"""
        x_x, y_y, z_z = select([stdin], [], [], 0)
        print(len(y_y))
        print(len(z_z))
        return len(x_x) != 0

    def get_from_stream(self):
        """getFromStream Method"""
        return stdin.read(1)

    def clear_stream(self):
        """ClearStream method"""
        tcflush(self.__fd, TCIFLUSH)

    def __del__(self):
        """Destructor"""
        tcsetattr(self.__fd, TCSANOW, self.__old)
