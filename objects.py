from board import *
import time


class Objects:

    def __init__(self):
        self.type = ""
        self.types = []
        self.symbols = []
        self.symbol_colors = []
        self.default_color = Back.LIGHTBLUE_EX + Style.BRIGHT
        self.position = {}
        self.purpose = ""
        self.spaces = []
        for i in range(100):
            self.spaces.append([' ']*30)

    def declare_position(self, x, y):
        self.position = {'x': x, 'y': y}

    def get_position(self):
        return self.position

    def shape_change(self):
        return

    def update_position(self, increment_x, increment_y):
        self.position = {'x': self.position['x'] + increment_x, 'y': self.position['y'] + increment_y}


class Cloud1(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.type = 'c'
        self.symbols = [[' ', '/', '\\'], ['/', ' ', ' ', '\\'], ['\\', '_', '_', '/']]
        for i in range(len(self.symbols)):
            self.symbol_colors.append([Back.LIGHTBLUE_EX + Fore.WHITE + Style.BRIGHT]*len(self.symbols[i]))
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Cloud2(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.type = 'c'
        self.symbols = [[' ', '/', '\\', '/', '\\', '/', '\\', ' '],
                        ['/', ' ', ' ', ' ', ' ', ' ', ' ', '\\'],
                        ['\\', '_', '_', '_', '_', '_', '_', '/']]
        for i in range(len(self.symbols)):
            self.symbol_colors.append([Back.LIGHTBLUE_EX + Fore.WHITE + Style.BRIGHT]*len(self.symbols[i]))
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Cloud3(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.type = 'c'
        self.symbols = [[' ', '/', '\\', '/', '\\', ' '],
                        ['/', ' ', ' ', ' ', ' ', '\\'],
                        ['\\', '_', '_', '_', '_', '/']]
        for i in range(len(self.symbols)):
            self.symbol_colors.append([Back.LIGHTBLUE_EX + Fore.WHITE + Style.BRIGHT]*len(self.symbols[i]))
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Mountain1(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.type = "m"
        self.symbols = [[' ', '/', '\\', '/', '\\', '/', '\\', ' '],
                        ['/', ' ', ' ', ' ', ' ', ' ', ' ', '\\']]
        for i in range(2):
            self.symbol_colors.append([Fore.LIGHTGREEN_EX+Back.LIGHTBLUE_EX+Style.BRIGHT]*8)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Mountain2(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.type = "m"
        self.symbols = [[' ', ' ', '_', '_', ' ', ' '],
                        [' ', '/', ' ', ' ', '\\', ' '],
                        ['/', ' ', ' ', ' ', ' ', '\\']]
        for i in range(3):
            self.symbol_colors.append([Fore.LIGHTGREEN_EX+Back.LIGHTBLUE_EX+Style.BRIGHT]*6)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Mountain3(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.type = "m"
        self.symbols = [[' ', '/', '\\', ' '],
                        ['/', ' ', ' ', '\\']
                        ]
        for i in range(2):
            self.symbol_colors.append([Fore.LIGHTGREEN_EX+Back.LIGHTBLUE_EX+Style.BRIGHT]*4)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Mountain4(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.type = "m"
        self.symbols = [[' ', ' ', ' ', ' ', '_', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' '],
                        [' ', ' ', '/', ' ', ' ', ' ', '\\', ' ', ' '],
                        [' ', '/', ' ', ' ', ' ', ' ', ' ', '\\', ' '],
                        ['/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\'],
                        ]
        for i in range(5):
            self.symbol_colors.append([Fore.LIGHTGREEN_EX+Back.LIGHTBLUE_EX+Style.BRIGHT]*9)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Brick1(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.type = "B1"
        self.brick_length = 3
        self.purpose = ""
        self.symbols = [[' ', 'X', ' '], [' ', 'X', ' ']]
        self.symbol_colors = [[Back.YELLOW, Back.YELLOW, Back.YELLOW],
                              [Back.YELLOW, Back.YELLOW, Back.YELLOW],
                              ]
        self.declare_position(x, y)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))

    def shape_change(self):
        if self.type == "B1":
            os.system('aplay -q sound/brick_smash.wav &')
            self.symbols = [[' ', ' ', ' '], [' ', ' ', ' ']]
            self.symbol_colors = [[Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX],
                                  [Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX],
                                  ]
            self.types = []
            for i in range(len(self.symbols)):
                self.types.append(["sky"]*len(self.symbols[i]))
            self.type = "sky"

        if self.type == "B2":
            os.system('aplay -q sound/coin.wav &')
            self.symbols = [[' ', 'X', ' '], [' ', 'X', ' ']]
            self.symbol_colors = [[Back.YELLOW, Back.YELLOW, Back.YELLOW],
                                  [Back.YELLOW, Back.YELLOW, Back.YELLOW],
                                  ]
            self.types = []
            for i in range(len(self.symbols)):
                self.types.append(["B1"]*len(self.symbols[i]))
            self.type = "B1"


class Mushroom(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.type = "mu"
        self.symbols = [['/', '\\'], ['|', '|']]
        self.symbol_colors = [[Fore.CYAN+Back.LIGHTBLUE_EX+Style.BRIGHT, Fore.CYAN+Back.LIGHTBLUE_EX+Style.BRIGHT],
                              [Fore.CYAN+Back.LIGHTBLUE_EX+Style.BRIGHT, Fore.CYAN + Back.LIGHTBLUE_EX+Style.BRIGHT],
                              ]
        self.declare_position(x, y)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))


class Brick2(Objects):

    def __init__(self, x, y, purpose):
        Objects.__init__(self)
        self.brick_length = 3
        self.purpose = purpose
        self.type = "B2"
        self.symbols = [[' ', '?', ' '], [' ', '?', ' ']]
        self.symbol_colors = [[Back.RED, Back.RED+Fore.WHITE, Back.RED],
                              [Back.RED, Back.RED+Fore.WHITE, Back.RED],
                              ]
        self.declare_position(x, y)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))

    def shape_change(self):
        if self.type == "B1":
            os.system('aplay -q sound/brick_smash.wav &')
            self.symbols = [[' ', ' ', ' '], [' ', ' ', ' ']]
            self.symbol_colors = [[Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX],
                                  [Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX],
                                  ]
            self.types = []
            for i in range(len(self.symbols)):
                self.types.append(["sky"]*len(self.symbols[i]))
            self.type = "sky"

        if self.type == "B2":
            os.system('aplay -q sound/coin.wav &')
            self.symbols = [[' ', 'X', ' '], [' ', 'X', ' ']]
            self.symbol_colors = [[Back.YELLOW, Back.YELLOW, Back.YELLOW],
                                  [Back.YELLOW, Back.YELLOW, Back.YELLOW],
                                  ]
            self.types = []
            for i in range(len(self.symbols)):
                self.types.append(["B1"]*len(self.symbols[i]))
            self.type = "B1"


class Pillar1(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.pillar_length = 5
        self.type = "P1"
        self.symbols = [[' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.symbol_colors = [[Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX],
                              [Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX]]
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Pillar2(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.pillar_length = 5
        self.type = "P2"
        self.symbols = [[' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.symbol_colors = [[Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX],
                              [Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX],
                              ]
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Pillar3(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.pillar_length = 5
        self.type = "P3"
        self.symbols = [[' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                       ]
        self.symbol_colors = [[Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX],
                              [Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX],
                              ]
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Gap(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.gap_length = 5
        self.type = "gap"
        self.symbols = [[' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                       ]
        self.symbol_colors = [[Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX],
                              [Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX, Back.LIGHTBLUE_EX],
                              ]
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Floor(Objects):

    def __init__(self, roll, x, y):
        Objects.__init__(self)
        self.type = "floor"
        for i in range(2):
            self.symbols.append(['_'] * roll.roll_x)
        for i in range(2):
            self.symbol_colors.append([Back.LIGHTRED_EX + Fore.BLACK] * roll.roll_x)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)


class Steps(Objects):

    def __init__(self, x, y, length, flag="left"):
        Objects.__init__(self)
        self.step_length = length * 2
        self.type = "sky"
        self.brown = '\033[1;43m_\033[1;m'
        self.declare_symbols(length, flag)
        for i in range(self.step_length):
            self.symbol_colors.append([Fore.BLACK+Back.LIGHTBLUE_EX+Style.BRIGHT]*self.step_length)
        self.declare_position(x, y)

    def reverse_steps(self):
        for symbol_list in self.symbols:
            symbol_list.reverse()
        time.sleep(2)

    def declare_symbols(self, length, flag):
        start = 2
        for i in range(length):
            temp = []
            temp1 = []
            if flag == "left":
                for j in range(self.step_length-start):
                    temp.append(' ')
                    temp1.append("sky")
                for k in range(start):
                    temp.append(self.brown)
                    temp1.append("S")
            else:
                for k in range(start):
                    temp.append(self.brown)
                    temp1.append("S")

                for j in range(self.step_length-start):
                    temp.append(' ')
                    temp1.append("sky")

            self.symbols.append(temp)
            self.symbols.append(temp)
            self.types.append(temp1)
            self.types.append(temp1)
            start += 2


class VerticalSteps(Objects):

    def __init__(self, x, y, length):
        Objects.__init__(self)
        self.step_length = length * 2
        self.type = "VS"
        self.brown = '\033[1;43m_\033[1;m'
        self.declare_symbols(length)
        for i in range(self.step_length):
            self.symbol_colors.append([Fore.BLACK+Back.LIGHTBLUE_EX+Style.BRIGHT]*2)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.declare_position(x, y)

    def declare_symbols(self, length):
        for i in range(length):
            self.symbols.append([self.brown]*2)
            self.symbols.append([self.brown]*2)


class Flag(Objects):

    def __init__(self, x, y, length):
        Objects.__init__(self)
        self.step_length = 1
        self.flag_length = 16
        self.type = "F"
        self.brown = '\033[1;43m_\033[1;m'
        self.declare_symbols(length)
        self.symbol_colors.append([Back.LIGHTBLUE_EX+Fore.BLACK])
        for i in range(length-1):
            self.symbol_colors.append([Fore.BLACK+Back.LIGHTGREEN_EX+Style.BRIGHT])
        self.declare_position(x, y)
        self.flag_paper = FlagPaper(x-4, y+1)
        self.flag_base = FlagBase(x-1, 19)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))

    def declare_symbols(self, length):
        self.symbols.append('O')
        for i in range(length-1):
            self.symbols.append([' '])


class FlagPaper(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.step_length = 2
        self.type = "FP"
        self.declare_position(x, y)
        self.symbols = [['_', '_', '_', '_'],
                        ['\\', ' ', '$', ' '],
                        [' ', '\\', '$', ' '],
                        [' ', ' ', '\\', '_']
                       ]
        for i in range(4):
            self.symbol_colors.append([Fore.WHITE+Back.LIGHTBLUE_EX+Style.BRIGHT]*4)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))
        self.symbol_colors[1][2] = Fore.BLACK+Back.LIGHTBLUE_EX
        self.symbol_colors[2][2] = Fore.BLACK+Back.LIGHTBLUE_EX


class FlagBase(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.step_length = 3
        self.brown = '\033[1;43m_\033[1;m'
        self.type = "FB"
        self.declare_position(x, y)
        for i in range(3):
            self.symbols.append([self.brown]*3)
        for i in range(3):
            self.symbol_colors.append([Style.BRIGHT]*3)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))


class Castle(Objects):

    def __init__(self, x, y):
        Objects.__init__(self)
        self.type = "C"
        self.brown = '\033[1;43m_\033[1;m'
        self.declare_symbols()
        self.declare_symbolcolors()
        self.declare_position(x, y)
        for i in range(len(self.symbols)):
            self.types.append([self.type]*len(self.symbols[i]))

    def declare_symbols(self):
        for i in range(10):
            self.symbols.append([self.brown]*17)

        for i in range(3):
            for j in range(4):
                self.symbols[i][j] = ' '

        for i in range(3):
            for j in range(13, 17):
                self.symbols[i][j] = ' '

        self.symbols[3][1] = ' '
        self.symbols[3][3] = ' '
        self.symbols[3][13] = ' '
        self.symbols[3][15] = ' '
        self.symbols[0][5] = ' '
        self.symbols[0][7] = ' '
        self.symbols[0][9] = ' '
        self.symbols[0][11] = ' '

        for i in range(2):
            for j in range(2):
                self.symbols[2+i][5+j] = ' '
                self.symbols[2+i][10+j] = ' '

        for i in range(3):
            for j in range(3):
                self.symbols[7+i][7+j] = ' '

    def declare_symbolcolors(self):
        for i in range(10):
            self.symbol_colors.append([Style.BRIGHT]*17)

        for i in range(3):
            for j in range(4):
                self.symbol_colors[i][j] = Back.LIGHTBLUE_EX

        for i in range(3):
            for j in range(13, 17):
                self.symbol_colors[i][j] = Back.LIGHTBLUE_EX

        self.symbol_colors[3][1] = Back.LIGHTBLUE_EX
        self.symbol_colors[3][3] = Back.LIGHTBLUE_EX
        self.symbol_colors[3][13] = Back.LIGHTBLUE_EX
        self.symbol_colors[3][15] = Back.LIGHTBLUE_EX
        self.symbol_colors[0][5] = Back.LIGHTBLUE_EX
        self.symbol_colors[0][7] = Back.LIGHTBLUE_EX
        self.symbol_colors[0][9] = Back.LIGHTBLUE_EX
        self.symbol_colors[0][11] = Back.LIGHTBLUE_EX

