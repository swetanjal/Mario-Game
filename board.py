from random import randint
from os import system
from time import sleep
from config import *

#Class for the scenery background.
class Board:
	#Sets up the scenery
	def __init__(self, BOARD_HEIGHT, BOARD_WIDTH):
		self.board = [[' ' for j in range(BOARD_WIDTH)]for i in range(BOARD_HEIGHT)]
		self.__BOARD_HEIGHT = BOARD_HEIGHT
		self.__BOARD_WIDTH = BOARD_WIDTH

	#Resets the board to empty
	def reint(self):
		self.board = [[' ' for j in range(BOARD_WIDTH)]for i in range(BOARD_HEIGHT)]
	
	#Function that redraws Mario on the terminal
	def draw_mario(self, mario):
		for i in range(MARIO_HEIGHT):
			for j in range(MARIO_WIDTH):
				self.board[mario.Y + i][mario.X + j] = 'F'
	#Function for displaying the scenery to the terminal
	def show(self, mario):
		system("clear")
		self.reint()
		self.draw_mario(mario)
		for i in range(BOARD_HEIGHT):
			s = ""
			for j in range(BOARD_HEIGHT):
				s = s + self.board[i][j]
			print(s)
		print()