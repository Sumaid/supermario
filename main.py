import os
import sys
import threading
import time
from input import Get, input_to
from board import *
from objects import *
from people import *
from levels import *
from colorama import Fore, Back, Style

if os.name == 'nt':
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]


class EnemyHandler:

    def __init__(self, enemies):
        self.enemies = enemies
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            for enemy in self.enemies:
                if enemy.alive:
                    enemy.move()
            time.sleep(0.2)


def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()


def show_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()


class Engine:

    def __init__(self, level):
        self.roll = Roll()
        self.board = Board(self.roll)
        self.level1 = Level(self.roll, self.board, level)
        self.player = Player(5, 20, self.board, self.roll)
        self.board.people_update(self.player, self.level1.enemies)
        self.board.people_renderer()

    def key_checker(self):
        getch = Get()
        start = 0
        while True:
            key_input = input_to(getch)
            if key_input == 'q':
                show_cursor()
                os.system('killall aplay')
                os.system('clear')
                sys.exit()

            if key_input == 'd':
                if time.time() - start > 0.1:
                    start = time.time()
                    next_input = input_to(getch)
                    if next_input == 'w':
                        os.system('aplay -q sound/small_jump.wav &')
                        os.system('clear')
                        cur = self.player.get_position()
                        if cur['x'] < 37:
                            self.player.jumpscene(1)
                        else:
                            self.player.jumpscene()
                    else:
                        self.player.move(2)

            elif key_input == 'a':
                if time.time() - start > 0.1:
                    start = time.time()
                    next_input = input_to(getch)
                    if next_input == 'w':
                        os.system('aplay -q sound/small_jump.wav &')
                        os.system('clear')
                        self.player.jumpscene(-1)
                    else:
                        self.player.move(-2)

            elif key_input == 'w':
                os.system('aplay -q sound/small_jump.wav  &')
                os.system('clear')
                if time.time() - start > 0.1:
                    start = time.time()
                    next_input = input_to(getch)
                    if next_input == 'd':
                        cur = self.player.get_position()
                        if cur['x'] < 37:
                            self.player.jumpscene(1)
                        else:
                            self.player.jumpscene()
                    elif next_input == 'a':
                        self.player.jumpscene(-1)
                    else:
                        self.player.vertical_jump(4)

            self.render()

    def render(self):
        self.board.initialize()
        self.board.people_renderer()
        self.board.print_board()

    def runner(self):
        hide_cursor()
        os.system('aplay -q sound/main_theme.wav &')
        self.render()
        self.eh = EnemyHandler(self.level1.enemies)
        self.key_checker()


if __name__ == '__main__':
    level = int(input('Choose level[1,2,3]:'))
    game_engine = Engine(level)
    game_engine.runner()
