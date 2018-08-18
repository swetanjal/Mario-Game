from person import *
from config import *
from fire import *
from random import randint
class Boss(Person):
	def __init__(self, X, Y, HEIGHT, WIDTH):
		Person.__init__(self, X, Y, HEIGHT, WIDTH)
		self.speed_X = -1
		self.speed_Y = -1
		self.iniX = X
		self.iniY = Y
		self.cnt = 0
	def update(self):
		if abs(self.X - self.iniX) > 12:
			self.speed_X = -self.speed_X
		if self.iniY - self.Y < 0:
			self.speed_Y = -self.speed_Y
		if self.iniY - self.Y > 12:
			self.speed_Y = -self.speed_Y
		self.X = self.X + self.speed_X
		self.Y = self.Y + self.speed_Y

	def fire_fire(self, mario, board):
		if abs(mario.X - self.X) < BOARD_WIDTH and self.cnt % 48 == 0:
			sp = 1
			if mario.X < self.X:
				sp = -1
			board.fire.append(Fire(self.X, self.Y + randint(3, 6), sp))
		self.cnt = self.cnt + 1