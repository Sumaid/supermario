from objects import *
from colorama import Fore, Back, Style
import time
import random
import os
import threading


class People(Objects):

    def __init__(self, board):
        Objects.__init__(self)
        self.board = board
        self.passible = ["c", "m", "sky", "gap"]
        self.enemy_passible = ["re", "se"]
        self.alive = True

    def update_position(self, increment_x, increment_y):
        self.position = {'x': self.position['x'] + increment_x, 'y': self.position['y'] + increment_y}

    def render(self):
        cur = self.get_position()
        if cur['x'] in range(0, self.board.size_x-2):
            self.board.board_update(self)


class Player(People):

    def __init__(self, x, y, board, roll):
        People.__init__(self, board)
        self.roll = roll
        self.status = "small"
        self.type = "P"
        self.hurtful = ["re", "be", "bullet"]
        self.alive = True
        self.symbols = [['^', '^'], ['o', 'o']]
        self.player_height = 2
        self.symbol_colors = [[Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX],
                              [Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX],
                              ]
        self.lsymbols = [['^', '^'], ['|', '|'], ['-', '-'], ['o', 'o']]
        self.lsymbol_colors = [[Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX],
                              [Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX],
                              [Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX],
                              [Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX],
                              ]
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)
        self.render()

    def restore(self, pointer=0):
        os.system('aplay -q sound/main_theme.wav &')
        self.declare_position(pointer+5, 20)
        self.alive = True

    def power_up(self):
        self.status = "large"
        self.symbols = self.lsymbols
        self.symbol_colors = self.lsymbol_colors
        self.player_height = 4
        self.types = []
        for i in range(len(self.lsymbols)):
            self.types.append([self.type]*len(self.lsymbols[i]))
        cur = self.get_position()
        self.declare_position(cur['x'], cur['y']-2)

    def power_down(self):
        self.status = "small"
        self.symbols = [['^', '^'], ['o', 'o']]
        self.player_height = 2
        self.symbol_colors = [[Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX],
                              [Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.WHITE + Style.BRIGHT + Back.LIGHTBLUE_EX],
                              ]
        self.types = []
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        cur = self.get_position()
        self.declare_position(cur['x'], cur['y']+2)

    def death(self):
        self.board.board_clear(self)
        self.alive = False

    def move(self, move):
        cur = self.get_position()
        if self.board.get_type(cur['x'] + move, cur['y']) in self.passible:
            if self.board.get_type(cur['x'] + move, cur['y'] + self.player_height) in self.passible:
                if cur['x'] > 37 and move > 0:
                    self.board.shift()
                    self.fall()
                else:
                    self.board.board_clear(self)
                    self.update_position(move, 0)
                    self.fall()
                    self.board.board_update(self)
            else:
                if cur['x'] > 37 and move > 0:
                    self.board.shift()
                else:
                    self.board.board_clear(self)
                    self.update_position(move, 0)
                    self.board.board_update(self)
        elif self.board.get_type(cur['x'] + move, cur['y']) == "mu":
            self.board.board_clear(self)
            self.update_position(move, 0)
            self.roll.roll_clear(self.board.get_reference(cur['x'] + move, cur['y']))
            self.board.print_board()
            self.power_up()
            os.system('aplay -q sound/powerup_appears.wav &')
            self.board.board_update(self)
            self.board.print_board()

        elif self.board.get_type(cur['x'] + move + 2, cur['y']) in self.hurtful:
            if self.board.player.status == "small":
                os.system('killall aplay')
                os.system('aplay -q sound/kick.wav')
                os.system('aplay -q sound/death.wav')
                self.death()
                time.sleep(1)
                self.restore()
                self.board.restore()
            else:
                os.system('aplay -q sound/pipe.wav &')
                self.power_down()
                enemy = self.board.get_reference(cur['x'] + move, cur['y'])
                enemy.update_position(enemy.speed, 0)
                self.board.board_update(self)
                self.board.board_update(enemy)
                self.board.print_board()

    def fall(self):
        cur = self.get_position()
        time_gap = 0.1
        i = 1
        y = cur['y']
        while self.board.get_type(cur['x'], y + self.player_height) in self.passible:
            self.board.board_clear(self)
            self.update_position(0, 1)
            self.board.board_update(self)
            self.board.people_renderer()
            self.board.print_board()
            y += 1
            i += 1
            time.sleep(time_gap)
            time_gap = 0.1/i

        if self.get_position()['y'] > 20:
            self.board.player.death()
            os.system('killall aplay')
            os.system('aplay -q sound/death.wav &')
            time.sleep(0.5)
            self.board.player.restore()
            self.board.restore()

        if self.board.get_type(cur['x'], y + self.player_height) in self.enemy_passible:
            enemy = self.board.get_reference(cur['x'], y + self.player_height)
            self.board.board_clear(enemy)
            enemy.alive = False
            os.system('aplay -q sound/stomp.wav &')
            self.board.board_clear(self)
            self.update_position(0, 2)
            self.board.board_update(self)
            self.board.score_update(200)
            self.board.people_renderer()
            self.board.print_board()

    def jumpscene(self, right=0):
        limit = 4
        time_gap = 0.1
        for i in range(limit, 0, -1):
            cur = self.get_position()
            if self.board.get_type(cur['x']+right, cur['y'] - i) in self.passible:
                self.board.board_clear(self)
                self.update_position(right, -i)
                if right == 0:
                    self.board.shift()
                self.board.board_update(self)
                self.board.people_renderer()
                self.board.print_board()
                time.sleep(time_gap)

        for i in range(limit*2):
            cur = self.get_position()
            y = cur['y']
            if cur['y'] + i > 22-self.player_height:
                if self.board.get_type(cur['x'], cur['y'] + i) not in self.passible:
                    self.update_position(0, 22-self.player_height-cur['y'])
                    self.board.people_renderer()
                    self.board.print_board()
                    return
                else:
                    y = cur['y']
                    flag = 0
                    while self.board.get_type(cur['x'], y + self.player_height + 1) == "gap":
                        self.board.board_clear(self)
                        self.update_position(0, 1)
                        self.board.board_update(self)
                        self.board.people_renderer()
                        self.board.print_board()
                        flag = 1
                        y += 1
                        time.sleep(time_gap)

                    if flag == 1:
                        self.board.player.death()
                        os.system('killall aplay')
                        os.system('aplay -q sound/death.wav &')
                        time.sleep(0.5)
                        os.system('clear')
                        self.board.player.restore()
                        self.board.restore()
                        self.board.print_board()
                        return

            for j in range(i + 1):
                if self.board.get_type(cur['x'] + right, cur['y'] + j + self.player_height) in self.enemy_passible or self.board.get_type(cur['x'], cur['y'] + j + self.player_height) in self.enemy_passible:
                    enemy = self.board.get_reference(cur['x'] + right, cur['y'] + j + self.player_height)
                    self.board.board_clear(enemy)
                    enemy.alive = False
                    self.board.board_clear(self)
                    self.update_position(right, 20-cur['y'])
                    if right == 0:
                        self.board.shift()
                    self.board.score_update(200)
                    self.board.board_update(self)
                    self.board.people_renderer()
                    self.board.print_board()
                    return
                elif self.board.get_type(cur['x'] + right, cur['y'] + j + self.player_height) == "be":
                    self.board.board_clear(self.board.boss)
                    self.board.boss.alive = False
                    self.board.print_board()

                elif self.board.get_type(cur['x'] + right, cur['y'] + j + self.player_height) not in self.passible:
                    self.board.board_clear(self)
                    self.update_position(right, j)
                    if right == 0:
                        self.board.shift()
                    self.board.board_update(self)
                    self.board.people_renderer()
                    self.board.print_board()
                    return

            if self.board.get_type(cur['x']+right, cur['y'] + i) in self.passible:
                self.board.board_clear(self)
                self.update_position(right, i)
                if right == 0:
                    self.board.shift()
                self.board.board_update(self)
                self.board.people_renderer()
                self.board.print_board()
                time.sleep(time_gap)

    def vertical_jump(self, limit):
        time_gap = 0.1/limit
        for i in range(10, 0, -1):
            cur = self.get_position()
            if self.board.get_type(cur['x']+1, cur['y'] - 1) in self.passible:
                self.board.board_clear(self)
                self.update_position(0, -1)
                self.board.board_update(self)
                self.board.people_renderer()
                self.board.print_board()
                time.sleep(time_gap)
                time_gap *= limit/i
            else:
                brick = self.board.get_reference(cur['x'] + 1, cur['y'] - 1)
                brick.shape_change()
                self.roll.roll_update(brick)
                self.board.coin_update(1)
                self.board.score_update(20)
                if brick.purpose == 'coin' and brick.type == 'B1':
                    cur = brick.get_position()
                    self.roll.symbol_update(cur['x']+1, cur['y']-1, 'O')
                    self.roll.color_update(cur['x']+1, cur['y']-1, Fore.RED+Style.BRIGHT+Back.LIGHTBLUE_EX)
                    self.board.initialize()
                    self.board.people_renderer()
                    self.board.print_board()
                    self.fall()
                    self.roll.symbol_update(cur['x']+1, cur['y']-1, ' ')
                    self.roll.color_update(cur['x']+1, cur['y']-1, Fore.WHITE+Style.BRIGHT+Back.LIGHTBLUE_EX)

                elif brick.purpose == 'power' and brick.type == 'B1':
                    cur = brick.get_position()
                    mushroom = Mushroom(cur['x'], cur['y']-2)
                    self.roll.roll_update(mushroom)
                    os.system('aplay -q sound/powerup_appears.wav &')
                    self.board.initialize()
                    self.board.people_renderer()
                    self.board.print_board()
                    self.fall()
                break
        self.fall()


class Enemies(People):

    def __init__(self, left, right, board):
        People.__init__(self, board)
        self.board = board
        self.path = {'left': left, 'right': right}

    def update_path(self, decrease):
        self.path = {'left': self.path['left'] + decrease, 'right': self.path['right'] + decrease}


class RegularEnemy(Enemies):

    def __init__(self, left, right, speed, board):
        Enemies.__init__(self, left, right, board)
        self.type = "re"
        self.symbols = [['[', ']'], ['/', '\\']]
        self.symbol_colors = [[Fore.LIGHTYELLOW_EX + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.LIGHTYELLOW_EX + Style.BRIGHT + Back.LIGHTBLUE_EX],
                              [Fore.LIGHTYELLOW_EX + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.LIGHTYELLOW_EX + Style.BRIGHT + Back.LIGHTBLUE_EX],
                              ]
        self.height = 2
        self.speed = speed
        self.left = left
        self.right = right
        self.declare_position(left, 22-self.height)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))

    def restore(self):
        self.path = {'left': self.left, 'right': self.right}
        self.declare_position(self.left, 22-self.height)

    def move1(self):
        if self.path['left'] < self.board.pointer + self.board.size_x:
            cur = self.get_position()
            if self.board.get_type(cur['x'] + self.speed, cur['y']) in self.passible and cur['x'] + self.speed in range(self.path['left'], self.path['right']+1):
                self.board.board_clear(self)
                self.update_position(self.speed, 0)
                self.board.board_update(self)
            elif self.board.get_type(cur['x'] + self.speed, cur['y']) == "none":
                self.update_position(self.speed, 0)
            elif self.board.get_type(cur['x'] + self.speed, cur['y']) == "P":
                self.board.player.death()
                time.sleep(1)
                self.board.player.restore()
                self.board.restore()
            else:
                self.speed = -self.speed
            self.board.initialize()

    def move(self):
        cur = self.get_position()
        if cur['x'] + self.speed in range(self.path['left'], self.path['right']+1):
            if self.board.get_type(cur['x'] + self.speed, cur['y']) == "P":
                if self.board.player.status == "small":
                    os.system('killall aplay')
                    os.system('aplay -q sound/kick.wav')
                    os.system('aplay -q sound/death.wav')
                    self.board.player.death()
                    time.sleep(1)
                    self.board.player.restore()
                    self.board.restore()
                else:
                    os.system('aplay -q sound/pipe.wav &')
                    self.board.player.power_down()
                    self.update_position(self.speed, 0)
                    self.board.board_update(self)
                    self.board.board_update(self.board.player)
                    self.board.print_board()

            elif self.board.get_type(cur['x'] + self.speed, cur['y']) == "none":
                self.update_position(self.speed, 0)
            elif self.board.get_type(cur['x'] + self.speed, cur['y']) in self.passible:
                if cur['x'] in range(0, self.board.size_x-4):
                    self.board.board_clear(self)
                self.update_position(self.speed, 0)
                if cur['x'] in range(0, self.board.size_x-4):
                    self.board.board_update(self)
            else:
                self.update_position(self.speed, 0)
        else:
            self.speed = -self.speed
        self.board.initialize()


class Bullet(Objects):

    def __init__(self, x, y, speed, board):
        Objects.__init__(self)
        self.board = board
        self.type = "bullet"
        self.status = "working"
        self.symbols = [['o']]
        self.symbol_colors = [[Fore.RED + Style.BRIGHT + Back.LIGHTBLUE_EX]]
        self.height = 1
        self.speed = speed
        self.declare_position(x, y)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.board.board_update(self)
        thread = threading.Thread(target=self.move, args=())
        thread.daemon = True
        thread.start()

    def render(self):
        cur = self.get_position()
        if cur['x'] in range(0, self.board.size_x):
            if self.status == "working":
                self.board.board_update(self)

    def move(self):
        while True:
            flag = 0
            self.board.board_clear(self)
            if self.get_position()['x']-self.speed > 0:
                for j in range(self.speed):
                    if self.board.get_type(self.get_position()['x']-j, self.get_position()['y']) == "P":
                        flag = 1
                        if self.board.player.status == "small":
                            os.system('killall aplay')
                            os.system('aplay -q sound/kick.wav')
                            os.system('aplay -q sound/death.wav')
                            self.board.player.death()
                            time.sleep(1)
                            self.board.player.restore(self.board.pointer)
                            self.board.restore(self.board.pointer)
                        else:
                            os.system('aplay -q sound/pipe.wav &')
                            self.board.player.power_down()
                            self.update_position(-self.speed, 0)
                            self.board.board_update(self)
                            self.board.board_update(self.board.player)
                            self.board.print_board()
                if flag == 0:
                    self.board.board_clear(self)
                    self.update_position(-self.speed, 0)
                    self.board.board_update(self)
            else:
                self.board.board_clear(self)
                self.status = "gone"
                break
            time.sleep(0.2)


class Boss(People):

    def __init__(self, x, y, board):
        People.__init__(self, board)
        self.type = "be"
        self.alive = False
        self.symbols = [['^', '^', '^'], ['<', 'o', '>'], ['<', 'o', '>']]
        self.symbol_colors = [[Fore.YELLOW + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.YELLOW + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.YELLOW + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               ],
                              [Fore.YELLOW + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.RED + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.YELLOW + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               ],
                              [Fore.YELLOW + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.RED + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               Fore.YELLOW + Style.BRIGHT + Back.LIGHTBLUE_EX,
                               ]
                             ]
        self.height = 3
        self.declare_position(x, y)
        self.bullets = []
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.thread = threading.Thread(target=self.fire, args=())
        self.thread.daemon = True
        self.thread.start()

    def render(self):
        cur = self.get_position()
        if cur['x'] in range(0, self.board.size_x):
            self.board.board_update(self)

    def fire(self):
        while True:
            self.bullets.append(Bullet(self.get_position()['x']-1, self.get_position()['y']+random.randint(1, 2), random.randint(1, 3), self.board))
            time.sleep(4)