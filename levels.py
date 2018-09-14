from colorama import Fore, Back, Style
import random
from objects import *
import time
from board import *
from people import *


class Levels:

    def __init__(self, roll):
        self.roll = roll
        self.clouds = []
        self.mountains = []
        self.bricks = []
        self.pillars = []
        self.steps = []
        self.floor = ""
        self.floor_gaps = []
        self.flags = []
        self.castles = []
        self.enemies = []
        self.boss = []

    def level_initialize(self):
        for cloud in self.clouds:
            self.roll.roll_update(cloud)
        for mountain in self.mountains:
            self.roll.roll_update(mountain)
        for brick in self.bricks:
            self.roll.roll_update(brick)
        for pillar in self.pillars:
            self.roll.roll_update(pillar)
        for step in self.steps:
            self.roll.roll_update(step)
        self.roll.roll_update(self.floor)
        for gap in self.floor_gaps:
            self.roll.roll_update(gap)
        for flag in self.flags:
            self.roll.roll_update(flag)
        for castle in self.castles:
            self.roll.roll_update(castle)
        for bossenemy in self.boss:
            self.roll.roll_update(bossenemy)


class Level(Levels):

    def __init__(self, roll,  board, difficulty):
        Levels.__init__(self, roll)
        self.clouds = [Cloud3(23, 3),
                       Cloud1(60, 4),
                       Cloud2(87, 3),
                       Cloud3(110, 4),
                       Cloud2(160, 5),
                       Cloud2(200, 5),
                       Cloud1(240, 5),
                       Cloud2(300, 3),
                       Cloud2(350, 4),
                       Cloud3(380, 5),
                       Cloud1(400, 3),
                       Cloud2(440, 4),
                       Cloud3(500, 3)
                       ]
        self.bricks = [Brick2(43, 13, 'coin'),
                       Brick2(55, 5, 'coin'),
                       Brick1(50, 13),
                       Brick2(53, 13, 'power'),
                       Brick1(56, 13),
                       Brick2(59, 13, 'coin'),
                       Brick1(62, 13),
                       Brick1(230, 13),
                       Brick2(233, 13, 'coin'),
                       Brick1(236, 13),
                       Brick1(239, 13),
                       Brick1(242, 5),
                       Brick1(245, 5),
                       Brick1(248, 5),
                       Brick1(251, 5),
                       Brick1(254, 5),
                       Brick1(257, 5),
                       Brick1(264, 5),
                       Brick1(267, 5),
                       Brick1(270, 5),
                       Brick2(273, 5, 'coin'),
                       Brick1(273, 13),
                       Brick1(288, 13),
                       Brick2(291, 13, 'coin'),
                       Brick2(303, 13, 'coin'),
                       Brick2(312, 13, 'coin'),
                       Brick2(312, 5, 'coin'),
                       Brick2(321, 13, 'coin'),
                       Brick1(337, 13),
                       Brick1(350, 5),
                       Brick1(353, 5),
                       Brick1(356, 5),
                       Brick1(368, 5),
                       Brick2(371, 5, 'coin'),
                       Brick2(374, 5, 'coin'),
                       Brick1(377, 5),
                       Brick1(371, 13),
                       Brick1(374, 13),
                       Brick1(487, 13),
                       Brick1(490, 13),
                       Brick2(493, 13, 'coin'),
                       Brick1(496, 13),
                       ]

        self.floor = Floor(self.roll, 0, 22)

        self.floor_gaps = [
                           Gap(195, 22),
                           Gap(254, 22),
                           Gap(450, 22)
                           ]

        self.steps = [
                      Steps(414, 14, 4, "right"),
                      Steps(440, 14, 4),
                      VerticalSteps(448, 14, 4),
                      Steps(456, 14, 4, "right"),
                      Steps(525, 6, 8),
                      VerticalSteps(540, 6, 8),
                      ]

        self.mountains = [Mountain1(15, 20),
                          Mountain3(55, 20),
                          Mountain2(100, 19),
                          Mountain1(150, 20),
                          Mountain4(210, 17),
                          Mountain1(240, 20),
                          Mountain2(260, 19),
                          Mountain3(300, 20),
                          Mountain4(360, 17),
                          Mountain4(400, 17),
                          Mountain1(430, 20),
                          Mountain2(480, 19)
                          ]

        self.pillars = [Pillar1(75, 18),
                        Pillar2(105, 16),
                        Pillar3(135, 14),
                        Pillar3(165, 14),
                        Pillar1(475, 18),
                        Pillar1(519, 18)
                        ]

        self.flags = [Flag(560, 4, 16)]

        self.castles = [Castle(580, 12)]

        self.enemies = [
                        RegularEnemy(25, 65, difficulty+1, board),
                        RegularEnemy(80, 105, difficulty+1, board),
                        RegularEnemy(140, 165, difficulty+1, board),
                        RegularEnemy(145, 165, difficulty+1, board),
                        RegularEnemy(200, 230, difficulty+1, board),
                        RegularEnemy(300, 360, difficulty+1, board),
                        RegularEnemy(480, 520, difficulty+1, board),
                        ]

        self.boss = []

        self.level_initialize()
