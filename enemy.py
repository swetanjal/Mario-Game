from person import *
from config import *
from random import randint
class Enemy(Person):
	def __init__(self, X, Y, speed = -1):
		Person.__init__(self, X, Y, ENEMY_HEIGHT, ENEMY_WIDTH)
		self.speed = speed
		self.cnt = -1
	def move(self, l_thresh, board, mario):
		
		if (board.board[self.Y][self.X + self.speed] == PIPE_SYMBOL or board.board[self.Y][self.X + self.width + self.speed] == PIPE_SYMBOL):
			self.speed = -self.speed
		if (self.speed >= 1):
			if board.board[self.Y + self.height][self.X + self.width + 1] == ' ':
				self.speed = -self.speed
		if self.speed <= -1:
			if board.board[self.Y + self.height][self.X - 1] == ' ':
				self.speed = -self.speed
		self.update(self.speed, 0, l_thresh, board, mario)