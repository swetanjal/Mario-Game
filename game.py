from get_input import *
from board import *
from config import *
import sys
import select
from termios import tcflush, TCIOFLUSH
from time import time, sleep
from mario import *
from person import *
#from brick import *

class Game:

	#Creates all the important elements of the game
	def __init__(self):
		self.__board = Board(BOARD_HEIGHT, BOARD_WIDTH)
		self.__mario = Mario(0, BOARD_HEIGHT - 3 - 3)

	def invalid(self):
		if self.__mario.Y >= BOARD_HEIGHT - 5 or self.__board.invalid(self.__mario) == True or self.__board.game_over == 1:
			print("GAME OVER!")
			return True
		return False
	#Starts a new game. This controls the flow of the game i.e accepts input, redraws the screen etc.
	def startNewGame(self):
		INPUT = Input()
		while True:
			if self.invalid():
				break
			sleep(1/12)
			if INPUT.checkStream():
				x = INPUT.getFromStream()
				INPUT.clearStream()
				if x == 'd':
					if self.__mario.jump_state == 1:
						self.__mario.update(3, Person.gravity[self.__mario.jump_idx], self.__board.left, self.__board, self.__mario)
					else:	
						self.__mario.update(1, 0, self.__board.left, self.__board, self.__mario)
				elif x == 'a':
					if self.__mario.jump_state == 1:
						self.__mario.update(-3, Person.gravity[self.__mario.jump_idx], self.__board.left, self.__board, self.__mario)
					else:
						self.__mario.update(-1, 0, self.__board.left, self.__board, self.__mario)	
				elif x == 'w' and self.__mario.jump_state == 0:
					self.__mario.jump_state = 1
					self.__mario.update(0, Person.gravity[self.__mario.jump_idx], self.__board.left, self.__board, self.__mario)
					#self.__mario.update(0, -1, self.__board.left)
				elif self.__mario.jump_state == 1:
					self.__mario.update(0, Person.gravity[self.__mario.jump_idx], self.__board.left, self.__board, self.__mario)
			elif self.__mario.jump_state == 1:
					if self.__mario.jump_idx < len(Person.gravity):
						self.__mario.update(0, Person.gravity[self.__mario.jump_idx], self.__board.left, self.__board, self.__mario)
			if self.invalid():
				break
			self.__board.show(self.__mario)
#Creates a Game object and starts the game
game = Game()
game.startNewGame()