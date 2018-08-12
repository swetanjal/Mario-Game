from get_input import *
from board import *
from config import *
import sys
import select
from termios import tcflush, TCIOFLUSH
from time import time, sleep
from mario import *

class Game:

	#Creates all the important elements of the game
	def __init__(self):
		self.__board = Board(BOARD_HEIGHT, BOARD_WIDTH)
		self.__mario = Mario(0, BOARD_HEIGHT - 2)
	
	#Starts a new game. This controls the flow of the game i.e accepts input, redraws the screen etc.
	def startNewGame(self):
		INPUT = Input()
		while True:
			sleep(0.1)
			if INPUT.checkStream():
				x = INPUT.getFromStream()
				INPUT.clearStream()
				if x == 'd':
					self.__mario.update(1,0)
				elif x == 'a':
					self.__mario.update(-1,0)
				else:
					self.__mario.update(0,-1)

			self.__board.show(self.__mario)

#Creates a Game object and starts the game
game = Game()
game.startNewGame()