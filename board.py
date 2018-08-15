from random import randint
from os import system
from time import sleep
from config import *
from brick import *
#Class for the scenery background.
class Board:
	#Sets up the scenery
	def __init__(self, BOARD_HEIGHT, BOARD_WIDTH):
		self.board = [[' ' for j in range(10 * BOARD_WIDTH)]for i in range(BOARD_HEIGHT)]
		self.bricks = []
		self.left = 0
		self.right = BOARD_WIDTH
		for i in range(20):
			t_X = randint(0, 5 * BOARD_WIDTH - 5)
			t_Y = BRICK_LEVEL_1
			leng = randint(1, 5)
			for j in range(leng):
				obj = Brick(t_X + j, t_Y)
				flag = 0
				for k in self.bricks:
					if k.X <= obj.X and obj.X <= k.X + 3 and k.Y <= obj.Y and obj.Y <= k.Y + 3:
						flag = 1
						break
				if flag == 0:
					self.bricks.append(obj)
		cnt = 0
		for i in range(0, 5 * BOARD_WIDTH, 3):
			if cnt == randint(10, 20):
				cnt = 0
				continue
			if cnt > 20:
				cnt = 0
				continue
			t_X = i
			t_Y = BOARD_HEIGHT - 3
			self.bricks.append(Brick(t_X, t_Y))
			cnt = cnt + 1
		self.__BOARD_HEIGHT = BOARD_HEIGHT
		self.__BOARD_WIDTH = BOARD_WIDTH

	#Resets the board to empty
	def reint(self):
		self.board = [[' ' for j in range(10 * BOARD_WIDTH)]for i in range(BOARD_HEIGHT)]	
	#Function that redraws Mario on the terminal
	def draw_mario(self, mario):
		for i in range(MARIO_HEIGHT):
			for j in range(MARIO_WIDTH):
				self.board[mario.Y + i][mario.X + j] = MARIO_SYMBOL
	#Function for displaying the scenery to the terminal
	def draw_bricks(self):
		for brick in self.bricks:
			for i in range(3):
				for j in range(3):
					self.board[brick.Y + i][brick.X + j] = BRICK_SYMBOL
	def show(self, mario):
		system("clear")
		self.reint()
		self.draw_mario(mario)
		self.draw_bricks()
		if mario.X > (self.left + self.right)/2:
			self.left = self.left + 1
			self.right = self.right + 1
		for i in range(BOARD_HEIGHT):
			s = ""
			for j in range(self.left, self.right):
				s = s + self.board[i][j]
			print(s)
		print()