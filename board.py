"""This file contains the implementation of the board for the game."""
import subprocess
from random import randint
from os import system
from colorama import Fore, Back
from config import *
from brick import Brick
from pipe import Pipe
from enemy import Enemy
from boss import Boss
from pole import Pole
from coin import Coin
# Class for the scenery background.


class Board:
    """Sets up the scenery"""

    def check_base(self, x_x, y_y, w_w, h_h):
        """Checks whether pipe can be rendered at this place."""
        for j in range(w_w):
            if self.board[y_y + h_h][x_x + j] == ' ':
                return False
        return True

    def __init__(self, level):
        """Constructor"""
        self.board = [[' ' for j in range(10 * BOARD_WIDTH)]
                      for i in range(BOARD_HEIGHT)]
        self.bricks = []
        self.pipes = []
        self.fire = []
        self.left = 0
        self.score = 0
        self.level = level
        self.right = BOARD_WIDTH
        self.game_over = 0
        self.boss = Boss(6 * BOARD_WIDTH, BOARD_HEIGHT - 3 -
                         BOSS_HEIGHT - 1, BOSS_HEIGHT, BOSS_WIDTH)
        self.pipes.append(Pipe(5, BOARD_HEIGHT - 3 - 4, 3, 4))
        self.pole = Pole(7 * BOARD_WIDTH, BOARD_HEIGHT - 3 - 12, 12)
        if self.level == 1:
            for x_x in range(0, 9 * BOARD_WIDTH, 60):
                for i in range(len(cloud)):
                    for j in range(len(cloud[i])):
                        self.board[15 + i][x_x + j] = cloud[i][j]
        else:
            for x_x in range(4, 9 * BOARD_WIDTH, 3):
                self.bricks.append(Brick(x_x, 15))
        for i in range(20):
            t_x = randint(0, 5 * BOARD_WIDTH - 5)
            t_y = BRICK_LEVEL_1
            leng = randint(1, 5)
            for j in range(leng):
                obj = Brick(t_x + j, t_y)
                flag = 0
                for k in self.bricks:
                    if(k.x_coord <= obj.x_coord and obj.x_coord <= k.x_coord + 2 \
                        and k.y_coord <= obj.y_coord and obj.y_coord <= k.y_coord + 3) \
                        or (k.x_coord <= obj.x_coord + 2 and obj.x_coord + 2 <= k.x_coord + 2 \
                            and k.y_coord <= obj.y_coord and obj.y_coord <= k.y_coord + 2):
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
            t_x = i
            t_y = BOARD_HEIGHT - 3
            self.bricks.append(Brick(t_x, t_y))
            cnt = cnt + 1
        cnt = 0
        self.draw_bricks()
        while cnt < 10:
            t_x = randint(4, 5 * BOARD_WIDTH - 5)
            t_h = randint(3, 5)
            t_y = BOARD_HEIGHT - 3 - t_h
            fl2 = 0
            for pipe in self.pipes:
                if (pipe.x_coord <= t_x and t_x <= pipe.x_coord + 3) \
                        or (pipe.x_coord <= t_x + 3 and t_x + 3 <= pipe.x_coord + 3):
                    fl2 = 1
                    break
            if fl2 == 0 and self.check_base(t_x, t_y, 3, t_h):
                self.pipes.append(Pipe(t_x, t_y, 3, t_h))
                cnt = cnt + 1
        cnt = 0
        self.enemies = []
        while cnt < 10:
            if self.create_enemy(randint(12, 5 * BOARD_WIDTH - 5)) is True:
                cnt = cnt + 1
        cnt = 0
        self.coins = []
        while cnt < 15 * self.level:
            x_x = randint(0, 6 * BOARD_WIDTH)
            y_y = BRICK_LEVEL_2
            f_l = 1
            for coin in self.coins:
                if coin.x_coord == x_x and coin.y_coord == y_y:
                    f_l = 0
            inv = 0
            for brick in self.bricks:
                if brick.y_coord == BRICK_LEVEL_1 \
                    and (abs(brick.x_coord - x_x) <= 3
                         or abs(x_x - brick.x_coord + 2) <= 3):
                    inv = 1
                    break
            if f_l == 1 and inv == 1:
                self.coins.append(Coin(x_x, y_y))
                cnt = cnt + 1
        #self.__BOARD_HEIGHT = BOARD_HEIGHT
        #self.__BOARD_WIDTH = BOARD_WIDTH
        self.level_up = 0

    def show_pole(self):
        """Displays pole object"""
        for i in range(self.pole.height):
            self.board[self.pole.y_coord + i][self.pole.x_coord] = POLE_SYMBOL

    def update_fire(self, mario):
        """Updates stae of fire object after every frame."""
        for fire in self.fire:
            fire.update(mario, self)

    def invalid(self, mario):
        """Checks whether Mario has dies or not."""
        if mario.y_coord >= BOARD_HEIGHT - 5:
            self.game_over = 1
            return True
        for enemy in self.enemies:
            if enemy.y_coord == mario.y_coord \
                and (enemy.x_coord == mario.x_coord
                     or enemy.x_coord == mario.x_coord + 1
                     or enemy.x_coord == mario.x_coord + 2
                     or enemy.x_coord + 2 == mario.x_coord
                     or enemy.x_coord + 2 == mario.x_coord + 1
                     or enemy.x_coord + 2 == mario.x_coord + 2):
                self.game_over = 1
                return True
        for i in range(mario.height):
            for j in range(mario.width):
                for k in range(self.boss.height):
                    for l_l in range(self.boss.width):
                        if mario.y_coord + i == self.boss.y_coord + k \
                                and mario.x_coord + j == self.boss.x_coord + l_l:
                            self.game_over = 1
                            return True
        for i in range(3):
            for j in range(3):
                for k in self.fire:
                    for l_l in range(2):
                        for m_m in range(2):
                            if mario.y_coord + i == k.y_coord + l_l \
                                    and mario.x_coord + j == k.x_coord + m_m:
                                self.game_over = 1
                                return True
        if mario.x_coord + 2 == self.pole.x_coord:
            self.level_up = 1
        return False

    def create_enemy(self, x_x):
        """Method handling the creation of enemies."""
        t_x = x_x
        t_y = BOARD_HEIGHT - 3 - ENEMY_HEIGHT
        f_l = 0
        for pipe in self.pipes:
            if pipe.x_coord == t_x or pipe.x_coord + 1 == t_x \
                    or pipe.x_coord + 2 == t_x or pipe.x_coord == t_x + 2 \
                    or pipe.x_coord + 1 == t_x + 2 or pipe.x_coord + 2 == t_x + 2:
                f_l = 1
                break
        for enemy in self.enemies:
            if (t_x >= enemy.x_coord and t_x <= enemy.x_coord + 2) \
                    or (t_x + 2 >= enemy.x_coord and t_x + 2 <= enemy.x_coord + 2):
                f_l = 1
                break
        if f_l == 0:
            self.enemies.append(Enemy(t_x, t_y))
            return True
        return False

    def play_brick_break(self):
        """Method handling playing of sound when a brick is broken."""
        self.brick_sound = subprocess.Popen(
            ["aplay", "-q", "./Sound/mario break brick sound effect (loud).wav"])

    def play_coin_collect(self):
        """Method handling playing of sound when coin collected."""
        self.coin_sound = subprocess.Popen(
            ["aplay", "-q", "./Sound/Super Mario Bros.-Coin Sound Effect.wav"])

    def check_collision(self, mario):
        """Checks collision with brick or coin object."""
        idx = -1
        cnt = 0
        for brick in self.bricks:
            if (brick.x_coord <= mario.x_coord and mario.x_coord <= brick.x_coord + 2 \
                and brick.y_coord <= mario.y_coord and mario.y_coord <= brick.y_coord + 2) \
                or (brick.x_coord <= mario.x_coord + 2 and mario.x_coord + 2 <= brick.x_coord + 2 \
                    and brick.y_coord <= mario.y_coord and mario.y_coord <= brick.y_coord + 2):
                idx = cnt
                break
            cnt = cnt + 1
        if idx != -1:
            self.play_brick_break()
            self.score = self.score + BRICK_SCORE
            del self.bricks[idx]
        idx = -1
        cnt = 0
        for brick in self.enemies:
            if (brick.x_coord <= mario.x_coord and mario.x_coord <= brick.x_coord + 2 \
                and brick.y_coord <= mario.y_coord + 2 and mario.y_coord + 2 <= brick.y_coord + 2) \
                or (brick.x_coord <= mario.x_coord + 2 and mario.x_coord + 2 <= brick.x_coord + 2 \
                    and brick.y_coord <= mario.y_coord + 2 \
                    and mario.y_coord + 2 <= brick.y_coord + 2):
                idx = cnt
                break
            cnt = cnt + 1
        if idx != -1:
            self.score = self.score + ENEMY_SCORE
            del self.enemies[idx]
        idx = -1
        cnt = 0
        for coin in self.coins:
            if (coin.x_coord == mario.x_coord or coin.x_coord == mario.x_coord + 1 \
                or coin.x_coord == mario.x_coord + 2) and (coin.y_coord == mario.y_coord \
                or coin.y_coord == mario.y_coord + 1 or coin.y_coord == mario.y_coord + 2):
                idx = cnt
                break
            cnt = cnt + 1
        if idx != -1:
            self.play_coin_collect()
            self.score = self.score + coin.points
            del self.coins[idx]

    def reint(self):
        """# Resets the board to empty"""
        self.board = [[' ' for j in range(10 * BOARD_WIDTH)]
                      for i in range(BOARD_HEIGHT)]
        if self.level == 1:
            for x in range(0, 9 * BOARD_WIDTH, 60):
                for i in range(len(cloud)):
                    for j in range(len(cloud[i])):
                        self.board[15 + i][x + j] = cloud[i][j]

    def draw_boss(self):
        """Renders boss on screen."""
        for i in range(BOSS_HEIGHT):
            for j in range(BOSS_WIDTH):
                self.board[self.boss.y_coord +
                           i][self.boss.x_coord + j] = BOSS_SYMBOL

    def draw_mario(self, mario):
        """Renders Mario on screen."""
        for i in range(MARIO_HEIGHT):
            for j in range(MARIO_WIDTH):
                self.board[mario.y_coord + i][mario.x_coord + j] = MARIO_SYMBOL

    def draw_bricks(self):
        """Renders bricks on the screen."""
        for brick in self.bricks:
            for i in range(3):
                for j in range(3):
                    self.board[brick.y_coord +
                               i][brick.x_coord + j] = BRICK_SYMBOL

    def draw_pipe(self):
        """Renders pipes on screen"""
        for pipe in self.pipes:
            for i in range(pipe.height):
                for j in range(pipe.width):
                    self.board[pipe.y_coord +
                               i][pipe.x_coord + j] = PIPE_SYMBOL

    def draw_enemies(self):
        """Renders enemies on the screen."""
        for enemy in self.enemies:
            for i in range(enemy.height):
                for j in range(enemy.width):
                    self.board[enemy.y_coord +
                               i][enemy.x_coord + j] = ENEMY_SYMBOL

    def update_enemies(self, mario):
        """Updates the state of enemies after each frame."""
        for enemy in self.enemies:
            enemy.move(self.left, self, mario)

    def draw_fire(self):
        """Renders fire object on screen."""
        for fire in self.fire:
            for i in range(2):
                for j in range(2):
                    self.board[fire.y_coord +
                               i][fire.x_coord + j] = FIRE_SYMBOL

    def draw_coins(self):
        """Renders coin object on screen."""
        for coin in self.coins:
            self.board[coin.y_coord][coin.x_coord] = COIN_SYMBOL

    def destruct(self):
        """Destroys fire object when it moves out of frame."""
        cnt = 0
        for fire in self.fire:
            if fire.x_coord + 2 > 7 * BOARD_WIDTH:
                del self.fire[cnt]
            cnt = cnt + 1

    def show(self, mario):
        """Puts everything together and renders game frame."""
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
        self.invalid(mario)
        if self.game_over != 1:
            self.check_collision(mario)
        self.draw_mario(mario)
        self.draw_coins()
        self.destruct()
        if mario.x_coord > (self.left + self.right)/2:
            self.left = self.left + 1
            self.right = self.right + 1
        for i in range(BOARD_HEIGHT):

            for j in range(self.left, self.right):
                if self.board[i][j] == MARIO_SYMBOL:
                    print(Fore.CYAN + self.board[i][j], end='')
                elif self.board[i][j] == 'B':
                    if i <= 18:
                        print(Fore.BLUE + self.board[i][j], end='')
                    elif i >= BOARD_HEIGHT - 3 or i < BOARD_HEIGHT - 9:
                        print(Fore.YELLOW + self.board[i][j], end='')
                    else:
                        print(Fore.GREEN + self.board[i][j], end='')
                elif self.board[i][j] == ENEMY_SYMBOL:
                    print(Fore.MAGENTA + self.board[i][j], end='')
                elif self.board[i][j] == ' ' and i > BOARD_HEIGHT - 3:
                    self.board[i][j] = '.'
                    print(Fore.BLUE + self.board[i][j], end='')
                elif self.board[i][j] == BOSS_SYMBOL:
                    print(Fore.RED + self.board[i][j], end='')
                elif self.board[i][j] == FIRE_SYMBOL:
                    print(Fore.RED + self.board[i][j], end='')
                elif self.board[i][j] == POLE_SYMBOL:
                    if self.level == 2:
                        print(Fore.YELLOW + self.board[i][j], end='')
                    else:
                        print(Fore.BLACK + self.board[i][j], end='')
                elif self.board[i][j] == PIPE_SYMBOL:
                    print(Fore.GREEN + self.board[i][j], end='')
                elif self.level == 2 and i >= BOARD_HEIGHT - 6 \
                        and i <= BOARD_HEIGHT - 3 and self.board[i][j] == ' ':
                    print(Back.BLACK + self.board[i][j], end='')
                elif self.board[i][j] == COIN_SYMBOL:
                    print(Fore.YELLOW + self.board[i][j], end='')
                elif self.board[i][j] == '[' or self.board[i][j] == ']':
                    print(Fore.BLUE + self.board[i][j], end='')
                else:
                    print(Fore.WHITE + self.board[i][j], end='')
                #s = s + self.board[i][j]
            print()
        print()
        print(Fore.WHITE + "YOUR SCORE = " + str(self.score))
        print()
