from colorama import Fore, Back, Style
import os
from main import *


class Roll:

    def __init__(self):
        self.roll_x = 600
        self.roll_y = 25
        self.roll_symbol = []
        self.roll_color = []
        self.roll_type = []
        self.roll_reference = []

        for i in range(self.roll_x):
            self.roll_symbol.append([' '] * self.roll_y)
            self.roll_color.append([Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT] * self.roll_y)
            self.roll_type.append(["sky"] * self.roll_y)
            self.roll_reference.append([""] * self.roll_y)

    def symbol_update(self, x, y, marker):
        self.roll_symbol[x][y] = marker

    def color_update(self, x, y, marker):
        self.roll_color[x][y] = marker

    def type_update(self, x, y, type):
        self.roll_type[x][y] = type

    def reference_update(self, x, y, entity):
        self.roll_reference[x][y] = entity

    def roll_update(self, entity):
        position = entity.get_position()
        for i in range(len(entity.symbols)):
            for j in range(len(entity.symbols[i])):
                self.symbol_update(position['x'] + j, position['y'] + i, entity.symbols[i][j])
                self.color_update(position['x'] + j, position['y'] + i, entity.symbol_colors[i][j])
                self.type_update(position['x'] + j, position['y'] + i, entity.types[i][j])
                self.reference_update(position['x'] + j, position['y'] + i, entity)

    def roll_clear(self, entity):
        position = entity.get_position()
        for i in range(len(entity.symbols)):
            for j in range(len(entity.symbols[i])):
                self.symbol_update(position['x'] + j, position['y'] + i, ' ')
                self.color_update(position['x'] + j, position['y'] + i, Fore.WHITE+Back.LIGHTBLUE_EX+Style.BRIGHT)
                self.type_update(position['x'] + j, position['y'] + i, 'sky')
                self.reference_update(position['x'] + j, position['y'] + i, '')


class Board:

    def __init__(self, roll):
        self.roll = roll
        self.pointer = 0
        self.blocks = []
        self.colors = []
        self.types = []
        self.references = []
        self.flag = 24
        self.size_x = 80
        self.size_y = 25
        self.score = "00000"
        self.stage = "1-1"
        self.coins = "000"
        self.lives = "3"
        self.mario_x = 10
        self.world_x = 30
        self.coin_x = 50
        self.lives_x = 70
        self.header_ordinate = 1
        self.mario_string = "MARIO"
        self.world_string = "WORLD"
        self.coin_string = "COINS"
        self.lives_string = "LIVES"
        self.boss = "none"
        for i in range(self.size_x):
            self.blocks.append([' ']*self.size_y)
        for i in range(self.size_x):
            self.colors.append([Back.LIGHTBLUE_EX + Style.BRIGHT]*self.size_y)
        for i in range(self.size_x):
            self.types.append(["sky"]*self.size_y)
        for i in range(self.size_x):
            self.references.append([""]*self.size_y)
        self.initialize()

    def symbol_update(self, x, y, marker):
        self.blocks[x][y] = marker

    def color_update(self, x, y, marker):
        self.colors[x][y] = marker

    def type_update(self, x, y, type):
        self.types[x][y] = type

    def reference_update(self, x, y, entity):
        self.references[x][y] = entity

    def get_symbol(self, x, y):
        return self.blocks[x][y]

    def get_color(self, x, y):
        return self.colors[x][y]

    def get_type(self, x, y):
        if x < 0 or y < 0 or x > self.size_x - 1 or y > self.size_y - 1:
            return "none"
        else:
            return self.types[x][y]

    def get_reference(self, x, y):
        return self.references[x][y]

    def score_update(self, increase):
        self.score = format((int(self.score) + increase), '05d')
        self.string_renderer(self.score, self.mario_x, self.header_ordinate+1)

    def coin_update(self, increase):
        self.coins = format((int(self.coins) + increase), '03d')
        self.string_renderer(self.coins, self.coin_x, self.header_ordinate+1)

    def stage_update(self):
        self.string_renderer(self.stage, self.world_x, self.header_ordinate+1)

    def lives_update(self, decrease):
        self.lives = format((int(self.lives) - decrease), '01d')
        self.string_renderer(self.lives, self.lives_x, self.header_ordinate+1)
        if self.lives == "0":
            os.system('killall aplay')
            os.system('clear')
            self.print_board()
            os.system('aplay -q sound/game_over.wav &')
            print('Game Over')
            time.sleep(1)
            show_cursor()
            sys.exit()

    def header_update(self):
        self.score_update(0)
        self.stage_update()
        self.coin_update(0)
        self.lives_update(0)
        self.string_renderer(self.mario_string, self.mario_x, self.header_ordinate)
        self.string_renderer(self.world_string, self.world_x, self.header_ordinate)
        self.string_renderer(self.coin_string, self.coin_x, self.header_ordinate)
        self.string_renderer(self.lives_string, self.lives_x, self.header_ordinate)

    def string_renderer(self, string, x, y):
        for i in range(len(string)):
            self.blocks[x+i][y] = string[i]

    def shift(self):
        if self.pointer > 500:
            self.boss = Boss(70, 19, self)
            self.boss.alive = True
            self.roll.roll_update(self.boss)

        for enemy in self.enemies:
            enemy.update_path(-1)
            enemy.update_position(-1, 0)
        for i in range(1, self.size_x-1):
            for j in range(3, self.size_y):
                self.blocks[i-1][j] = self.blocks[i][j]
                self.colors[i-1][j] = self.colors[i][j]
                self.types[i-1][j] = self.types[i][j]
                self.references[i-1][j] = self.references[i][j]

        for j in range(3, self.size_y):
            self.blocks[self.size_x-1][j] = self.roll.roll_symbol[self.flag+1][j]
            self.colors[self.size_x-1][j] = self.roll.roll_color[self.flag+1][j]
            self.types[self.size_x-1][j] = self.roll.roll_type[self.flag+1][j]
            self.references[self.size_x-1][j] = self.roll.roll_reference[self.flag+1][j]

        self.pointer = self.pointer + 1

        self.flag += 1

    def initialize(self):
        for i in range(self.size_x):
            for j in range(self.size_y):
                self.blocks[i][j] = self.roll.roll_symbol[self.pointer+i][j]
                self.colors[i][j] = self.roll.roll_color[self.pointer+i][j]
                self.types[i][j] = self.roll.roll_type[self.pointer+i][j]
                self.references[i][j] = self.roll.roll_reference[self.pointer+i][j]

        self.flag = self.size_y - 1
        self.header_update()

    def restore(self, pointer=0):
        self.pointer = pointer
        self.lives_update(1)
        for enemy in self.enemies:
            enemy.restore()
        self.initialize()

    def people_renderer(self):
        if self.player.alive:
            self.player.render()
        for enemy in self.enemies:
            if enemy.alive:
                enemy.render()

        if self.boss != "none":
            self.boss.render()
            for bullet in self.boss.bullets:
                bullet.render()

    def people_update(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def board_update(self, entity):
        position = entity.get_position()
        for i in range(len(entity.symbols)):
            for j in range(len(entity.symbols[i])):
                self.symbol_update(position['x'] + j, position['y'] + i, entity.symbols[i][j])
                self.color_update(position['x'] + j, position['y'] + i, entity.symbol_colors[i][j])
                self.type_update(position['x'] + j, position['y'] + i, entity.types[i][j])
                self.reference_update(position['x'] + j, position['y'] + i, entity)

    def board_clear(self, entity):
        position = entity.get_position()
        for i in range(len(entity.symbols)):
            for j in range(len(entity.symbols[i])):
                self.symbol_update(position['x'] + j, position['y'] + i, ' ')
                self.color_update(position['x'] + j, position['y'] + i, Back.LIGHTBLUE_EX + Style.BRIGHT)
                self.type_update(position['x'] + j, position['y'] + i, "sky")
                self.reference_update(position['x'] + j, position['y'] + i, "")

    def print_board(self):
        os.system('clear')
        for j in range(self.size_y-1):
            for i in range(self.size_x):
                print(self.colors[i][j] + self.blocks[i][j] + Style.RESET_ALL, end="")
            print('')
