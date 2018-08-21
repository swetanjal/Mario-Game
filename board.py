from random import randint
from os import system
from time import sleep
from config import *
from brick import *
from pipe import *
from enemy import *
from boss import *
from pole import * 
import subprocess
from colorama import Fore, Back
#Class for the scenery background.
class Board:
	#Sets up the scenery
	def check_base(self, x, y, w, h):
		for j in range(w):
			if self.board[y + h][x + j] == ' ':
				return False
		return True
	def __init__(self, BOARD_HEIGHT, BOARD_WIDTH, level):
		self.board = [[' ' for j in range(10 * BOARD_WIDTH)]for i in range(BOARD_HEIGHT)]
		self.bricks = []
		self.pipes = []
		self.fire = []
		self.left = 0
		self.level = level
		self.right = BOARD_WIDTH
		self.game_over = 0
		self.boss = Boss(6 * BOARD_WIDTH, BOARD_HEIGHT - 3 - BOSS_HEIGHT - 1, BOSS_HEIGHT, BOSS_WIDTH)
		self.pipes.append(Pipe(4, BOARD_HEIGHT - 3 - 4, 3, 4))
		self.pole = Pole(7 * BOARD_WIDTH, BOARD_HEIGHT - 3 - 12, 12)
		for x in range(0, 9 * BOARD_WIDTH, 60):
			for i in range(len(cloud)):
				for j in range(len(cloud[i])):
					self.board[15 + i][x + j] = cloud[i][j]
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
		fll = 0
		for i in range(0, 10 * BOARD_WIDTH, 3):
			if cnt == randint(10, 20) or fll == 1:
				cnt = 0
				if self.level == 2:
					fll = 1 - fll
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
		self.level_up = 0	
	def show_pole(self):
		for i in range(self.pole.height):
			self.board[self.pole.Y + i][self.pole.X] = POLE_SYMBOL
	def update_fire(self, mario):
		for fire in self.fire:
			fire.update(mario, self)

	def invalid(self, mario):
		if mario.Y >= BOARD_HEIGHT - 5:
			self.game_over = 1
			return True
		for enemy in self.enemies:
			if enemy.Y == mario.Y and (enemy.X == mario.X or enemy.X == mario.X + 1 or enemy.X == mario.X + 2 or enemy.X + 2 == mario.X or enemy.X + 2 == mario.X + 1 or enemy.X + 2 == mario.X + 2):
				self.game_over = 1
				return True
		for i in range(mario.height):
			for j in range(mario.width):
				for k in range(self.boss.height):
					for l in range(self.boss.width):
						if mario.Y + i == self.boss.Y + k and mario.X + j == self.boss.X + l:
							self.game_over = 1
							return True
		for i in range(3):
			for j in range(3):
					for k in self.fire:
						for l in range(2):
							for m in range(2):
								if mario.Y + i == k.Y + l and mario.X + j == k.X + m:
									self.game_over = 1
									return True
		if mario.X + 2 == self.pole.X:
			self.level_up = 1
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
	def play_brick_break(self):
		self.brick_sound = subprocess.Popen(["aplay", "-q", "./mario break brick sound effect (loud).wav"])
	def check_collision(self, mario):
		idx = -1
		cnt = 0
		for brick in self.bricks:
			if (brick.X <= mario.X and mario.X <= brick.X + 2 and brick.Y <= mario.Y and mario.Y <= brick.Y + 2) or (brick.X <= mario.X + 2 and mario.X + 2 <= brick.X + 2 and brick.Y <= mario.Y and mario.Y <= brick.Y + 2):
				idx = cnt
				break
			cnt = cnt + 1
		if idx != -1:
			self.play_brick_break()
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
		for x in range(0, 9 * BOARD_WIDTH, 60):
			for i in range(len(cloud)):
				for j in range(len(cloud[i])):
					self.board[15 + i][x + j] = cloud[i][j]	
	#Function that redraws Mario on the terminal
	def draw_boss(self):
		for i in range(BOSS_HEIGHT):
			for j in range(BOSS_WIDTH):
				self.board[self.boss.Y + i][self.boss.X + j] = BOSS_SYMBOL

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

	def draw_fire(self):
		for fire in self.fire:
			for i in range(2):
				for j in range(2):
					self.board[fire.Y + i][fire.X + j] = FIRE_SYMBOL

	def destruct(self):
		cnt = 0
		for fire in self.fire:
			if fire.X + 2 > 7 * BOARD_WIDTH:
				del self.fire[cnt]
			cnt = cnt + 1
	def show(self, mario):
		system("clear")
		self.boss.update(mario)
		self.update_enemies(mario)
		self.reint()
		self.draw_mario(mario)
		self.draw_bricks()
		self.draw_pipe()
		self.draw_boss()
		self.show_pole()
		self.draw_enemies()
		if self.level == 2:
			self.boss.fire_fire(mario, self)
		self.update_fire(mario)
		self.draw_fire()
		self.check_collision(mario)
		self.invalid(mario)
		self.draw_mario(mario)
		self.destruct()
		if mario.X > (self.left + self.right)/2:
			self.left = self.left + 1
			self.right = self.right + 1
		for i in range(BOARD_HEIGHT):
			s = ""
			for j in range(self.left, self.right):
				if self.board[i][j] == MARIO_SYMBOL:
					print(Fore.CYAN + self.board[i][j], end='')
				elif self.board[i][j] == 'B':
					if i >= BOARD_HEIGHT - 3 or i < BOARD_HEIGHT - 9:
						print(Fore.YELLOW + self.board[i][j], end = '')
					else:
						print(Fore.GREEN + self.board[i][j], end = '')
				elif self.board[i][j] == ENEMY_SYMBOL:
					print(Fore.MAGENTA + self.board[i][j], end = '')
				elif self.board[i][j] == ' ' and i > BOARD_HEIGHT - 3:
					self.board[i][j] = '.'
					print(Fore.BLUE + self.board[i][j], end = '')
				elif self.board[i][j] == BOSS_SYMBOL:
					print(Fore.RED + self.board[i][j], end = '')
				elif self.board[i][j] == FIRE_SYMBOL:
					print(Fore.RED + self.board[i][j], end = '')
				elif self.board[i][j] == POLE_SYMBOL:
					if self.level == 2:
						print(Fore.YELLOW + self.board[i][j], end = '')
					else:	
						print(Fore.BLACK + self.board[i][j], end = '')
				elif self.board[i][j] == PIPE_SYMBOL:
					print(Fore.GREEN + self.board[i][j], end = '')
				elif self.level == 2 and i >= BOARD_HEIGHT - 6 and i <= BOARD_HEIGHT - 3 and self.board[i][j] == ' ':
					print(Back.BLACK + self.board[i][j], end = '') 
				else:
					print(Fore.WHITE + self.board[i][j], end = '')
				#s = s + self.board[i][j]
			print()
		print()