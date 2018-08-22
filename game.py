from get_input import *
from board import *
from config import *
import sys
import select
from termios import tcflush, TCIOFLUSH
from time import time, sleep
from mario import *
from person import *
from colorama import Fore, Back
#from brick import *
import subprocess
import time
class Game:

	#Creates all the important elements of the game
	def __init__(self, level):
		self.__board = Board(BOARD_HEIGHT, BOARD_WIDTH, level)
		self.__level = level
		self.ini_time = time.clock()
		if level == 2:
			self.__mario = Mario(1, BOARD_HEIGHT - 3 - 3 - 30)
			self.__mario.update(0, 0, 0, self.__board, self.__mario)
		else:	
			self.__mario = Mario(0, BOARD_HEIGHT - 3 - 3)
		if level == 1:
			self.bg_music = subprocess.Popen(["aplay", "-q", "./Sound/Super Mario Bros. Soundtrack.wav"])
		else:
			self.bg_music = subprocess.Popen(["aplay", "-q", "./Sound/Super Mario Underground Themes 1985 - 2010.wav"])
		self.win = 0
	def invalid(self):
		if self.__board.level_up == 1:
			self.bg_music.kill()
			self.jump_music.kill()
			self.play_win_music()
			sleep(2)
			if self.__level == 1:
				now = time.clock()
				penalty = now - self.ini_time
				print("YOUR FINAL SCORE = " + str(self.__board.score - (penalty/10)))
				print()
				print(Fore.RED + "CONGRATULATIONS! YOU PROGRESS TO NEXT LEVEL!!!")
				
			else:
				now = time.clock()
				penalty = now - self.ini_time
				print("YOUR FINAL SCORE = " + str(self.__board.score - (penalty/10)))
				print()
				print(Fore.RED + "YOU WIN!")

			self.win = 1
			return True
		if self.__board.game_over == 1:
			self.bg_music.kill()
			self.jump_music.kill()
			self.play_death_music()
			now = time.clock()
			penalty = now - self.ini_time
			sleep(2)
			print("YOUR FINAL SCORE = " + str(self.__board.score - (penalty/10)))
			print()
			print(Fore.RED + "GAME OVER!")
			#sleep(1)
			return True
		return False
	#Starts a new game. This controls the flow of the game i.e accepts input, redraws the screen etc.
	def play_death_music(self):
		self.bg_music = subprocess.Popen(["aplay", "-q", "./Sound/Super Mario Death Sound - Sound Effect.wav"])
	def play_win_music(self):
		self.win_music = subprocess.Popen(["aplay", "-q", "./Sound/Super Mario Bros. Music - Level Complete.wav"])
	def play_jump_music(self):
		self.jump_music = subprocess.Popen(["aplay", "-q", "./Sound/Mario jump sound effect +free download.wav"])
	def startNewGame(self):
		INPUT = Input()
		while True:
			if self.invalid():
				break
			sleep(1/12)
			if INPUT.checkStream():
				x = INPUT.getFromStream()
				INPUT.clearStream()
				if x == 'q':
					break
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
					self.play_jump_music()
					self.__mario.update(0, Person.gravity[self.__mario.jump_idx], self.__board.left, self.__board, self.__mario)
					#self.__mario.update(0, -1, self.__board.left)
				elif self.__mario.jump_state == 1:
					self.__mario.update(0, Person.gravity[self.__mario.jump_idx], self.__board.left, self.__board, self.__mario)
			elif self.__mario.jump_state == 1:
					if self.__mario.jump_idx < len(Person.gravity):
						self.__mario.update(0, Person.gravity[self.__mario.jump_idx], self.__board.left, self.__board, self.__mario)
			self.__board.show(self.__mario)
			self.__board.invalid(self.__mario)
			if self.invalid():
				break
#Creates a Game object and starts the game
game = Game(1)
game.startNewGame()
sleep(2)
game.bg_music.kill()
if game.win == 1:
	sleep(7)
	game2 = Game(2)
	game2.startNewGame()