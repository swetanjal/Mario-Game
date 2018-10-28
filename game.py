"""Starts a new game. This controls the flow of the game i.e accepts input,
redraws the screen etc."""
import subprocess
import time
from colorama import Fore, Back
from get_input import Input
from board import Board
from config import BOARD_HEIGHT

from time import sleep
from mario import Mario
from person import Person


class Game:

    """Creates all the important elements of the game"""
    def __init__(self, level):
        """Constructor"""
        self.__board = Board(level)
        self.__level = level
        self.ini_time = time.clock()
        if level == 2:
            self.__mario = Mario(1, BOARD_HEIGHT - 3 - 3 - 30)
            self.__mario.update(0, 0, 0, self.__board, self.__mario)
        else:
            self.__mario = Mario(0, BOARD_HEIGHT - 3 - 3)
        if level == 1:
            self.bg_music = subprocess.Popen(
                ["aplay", "-q", "./Sound/Super Mario Bros. Soundtrack.wav"])
        else:
            self.bg_music = subprocess.Popen(
                ["aplay", "-q", "./Sound/Super Mario Underground Themes 1985 - 2010.wav"])
        self.win = 0

    def invalid(self):
        """Checks if game is over or not"""
        if self.__board.level_up == 1:
            self.bg_music.kill()
            self.jump_music.kill()
            self.play_win_music()
            sleep(2)
            if self.__level == 1:
                now = time.clock()
                penalty = now - self.ini_time
                print("YOUR FINAL SCORE = " +
                      str(self.__board.score - (penalty/10)))
                print()
                print(Fore.RED + "CONGRATULATIONS! YOU PROGRESS TO NEXT LEVEL!!!")

            else:
                now = time.clock()
                penalty = now - self.ini_time
                print("YOUR FINAL SCORE = " +
                      str(self.__board.score - (penalty/10)))
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
            # sleep(1)
            return True
        return False

    def play_death_music(self):
        """This method plays sound when Mario dies."""
        self.bg_music = subprocess.Popen(
            ["aplay", "-q", "./Sound/Super Mario Death Sound - Sound Effect.wav"])

    def play_win_music(self):
        """This method plays the sound when Mario completes a level."""
        self.win_music = subprocess.Popen(
            ["aplay", "-q", "./Sound/Super Mario Bros. Music - Level Complete.wav"])

    def play_jump_music(self):
        """This method plays the jump sound."""
        self.jump_music = subprocess.Popen(
            ["aplay", "-q", "./Sound/Mario jump sound effect +free download.wav"])

    def start_new_game(self):
        """This method starts a new game."""
        INPUT = Input()
        while True:
            if self.invalid():
                break
            sleep(1/12)
            if INPUT.check_stream():
                x = INPUT.get_from_stream()
                INPUT.clear_stream()
                if x == 'q':
                    break
                if x == 'd':
                    if self.__mario.jump_state == 1:
                        self.__mario.update(
                            3, Person.gravity[self.__mario.jump_idx],
                            self.__board.left, self.__board, self.__mario)
                    else:
                        self.__mario.update(
                            1, 0, self.__board.left, self.__board, self.__mario)
                elif x == 'a':
                    if self.__mario.jump_state == 1:
                        self.__mario.update(-3, Person.gravity[self.__mario.jump_idx],
                                            self.__board.left, self.__board, self.__mario)
                    else:
                        self.__mario.update(-1, 0, self.__board.left,
                                            self.__board, self.__mario)
                elif x == 'w' and self.__mario.jump_state == 0:
                    self.__mario.jump_state = 1
                    self.play_jump_music()
                    self.__mario.update(
                        0, Person.gravity[self.__mario.jump_idx],
                        self.__board.left, self.__board, self.__mario)
                    #self.__mario.update(0, -1, self.__board.left)
                elif self.__mario.jump_state == 1:
                    self.__mario.update(
                        0, Person.gravity[self.__mario.jump_idx],
                        self.__board.left, self.__board, self.__mario)
            elif self.__mario.jump_state == 1:
                if self.__mario.jump_idx < len(Person.gravity):
                    self.__mario.update(
                        0, Person.gravity[self.__mario.jump_idx],
                        self.__board.left, self.__board, self.__mario)
            self.__board.show(self.__mario)
            self.__board.invalid(self.__mario)
            if self.invalid():
                break


# Creates a Game object and starts the game
GAME = Game(1)
GAME.start_new_game()
sleep(2)
GAME.bg_music.kill()
if GAME.win == 1:
    sleep(7)
    GAME2 = Game(2)
    GAME2.start_new_game()
