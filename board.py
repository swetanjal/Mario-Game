from random import randint
from os import system
from time import sleep
from config import *
from brick import *
from pipe import *
from enemy import *
#Class for the scenery background.
class Board:
	#Sets up the scenery
	def check_base(self, x, y, w, h):
		for j in range(w):
			if self.board[y + h][x + j] == ' ':
				return False
		return True
	def __init__(self, BOARD_HEIGHT, BOARD_WIDTH):
		self.board = [[' ' for j in range(10 * BOARD_WIDTH)]for i in range(BOARD_HEIGHT)]
		self.bricks = []
		self.pipes = []
		self.left = 0
		self.right = BOARD_WIDTH
		self.game_over = 0
		for i in range(20):
			t_X = randint(0, 5 * BOARD_WIDTH - 5)
			t_Y = BRICK_LEVEL_1
			leng = randint(1, 5)
			for j in range(leng):
				obj = Brick(t_X + j, t_Y)
				flag = 0
				for k in self.bricks:
					if (k.X <= obj.X and obj.X <= k.X + 2 and k.Y <= obj.Y and obj.Y <= k.Y + 3) or (k.X <= obj.X +2 and obj.X + 2 <= k.X + 2 and k.Y <= obj.Y and obj.Y <= k.Y + 2):
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
		cnt = 0
		self.draw_bricks()
		while cnt < 10:
			t_X = randint(4, 5 * BOARD_WIDTH - 5)
			t_h = randint(3, 5)
			t_Y = BOARD_HEIGHT - 3 - t_h
			fl2 = 0
			for pipe in self.pipes:
				if (pipe.X <= t_X and t_X <= pipe.X + 3) or (pipe.X <= t_X + 3 and t_X + 3 <= pipe.X + 3):
					fl2 = 1
					break 
			if fl2 == 0 and self.check_base(t_X, t_Y, 3, t_h):
				self.pipes.append(Pipe(t_X, t_Y, 3, t_h))
				cnt = cnt + 1
		cnt = 0
		self.enemies = []
		while cnt < 10:
			if self.create_enemy(randint(12, 5 * BOARD_WIDTH - 5)) == True:		
				cnt = cnt + 1
		self.__BOARD_HEIGHT = BOARD_HEIGHT
		self.__BOARD_WIDTH = BOARD_WIDTH
	
	def invalid(self, mario):
		for enemy in self.enemies:
			if enemy.Y == mario.Y and (enemy.X == mario.X or enemy.X == mario.X + 1 or enemy.X == mario.X + 2 or enemy.X + 2 == mario.X or enemy.X + 2 == mario.X + 1 or enemy.X + 2 == mario.X + 2):
				self.game_over = 1
				return True
		return False

	def create_enemy(self, X):
		t_X = X
		t_Y = BOARD_HEIGHT - 3 - ENEMY_HEIGHT
		fl = 0
		for pipe in self.pipes:
			if pipe.X == t_X or pipe.X + 1 == t_X or pipe.X + 2 == t_X or  pipe.X == t_X + 2 or pipe.X + 1 == t_X + 2 or pipe.X + 2 == t_X + 2:
				fl = 1
				break
		for enemy in self.enemies:
			if (t_X >= enemy.X and t_X <= enemy.X + 2) or (t_X + 2 >= enemy.X and t_X + 2 <= enemy.X + 2):
				fl = 1
				break
		if fl == 0:
			self.enemies.append(Enemy(t_X, t_Y))
			return True
		return False
	
	def check_collision(self, mario):
		idx = -1
		cnt = 0
		for brick in self.bricks:
			if (brick.X <= mario.X and mario.X <= brick.X + 2 and brick.Y <= mario.Y and mario.Y <= brick.Y + 2) or (brick.X <= mario.X + 2 and mario.X + 2 <= brick.X + 2 and brick.Y <= mario.Y and mario.Y <= brick.Y + 2):
				idx = cnt
				break
			cnt = cnt + 1
		if idx != -1:
			del self.bricks[idx]
		idx = -1
		cnt = 0
		for brick in self.enemies:
			if (brick.X <= mario.X and mario.X <= brick.X + 2 and brick.Y <= mario.Y + 2 and mario.Y + 2 <= brick.Y + 2) or (brick.X <= mario.X + 2 and mario.X + 2 <= brick.X + 2 and brick.Y <= mario.Y + 2 and mario.Y + 2 <= brick.Y + 2):
				idx = cnt
				break
			cnt = cnt + 1
		if idx != -1:
			del self.enemies[idx]
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
	def draw_pipe(self):
		for pipe in self.pipes:
			for i in range(pipe.height):
				for j in range(pipe.width):
					self.board[pipe.Y + i][pipe.X + j] = PIPE_SYMBOL

	def draw_enemies(self):
		for enemy in self.enemies:
			for i in range(enemy.height):
				for j in range(enemy.width):
					self.board[enemy.Y + i][enemy.X + j] = ENEMY_SYMBOL
	def update_enemies(self, mario):
		for enemy in self.enemies:
			enemy.move(self.left, self, mario)

	def show(self, mario):
		system("clear")
		self.update_enemies(mario)
		self.reint()
		self.draw_mario(mario)
		self.draw_bricks()
		self.draw_pipe()
		self.draw_enemies()
		self.check_collision(mario)
		if mario.X > (self.left + self.right)/2:
			self.left = self.left + 1
			self.right = self.right + 1
		for i in range(BOARD_HEIGHT):
			s = ""
			for j in range(self.left, self.right):
				s = s + self.board[i][j]
			print(s)
		print()