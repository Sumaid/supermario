# Super Mario Python Terminal Game

This is a clone of Super Mario Bros game. First level of this game is made as close as possible to original game.This is purely terminal game.I didn't use any pygame or curses like library which made this game development very challenging.

Tools Used:
	Python 3.6
	Colorama Library

Instruction to open:
	- python3 main.py

Game Controls:
	- Use a,d for left and right movement.
	- w for vertical jump
	- w+a or a+w for left jump, w+d or d+w for right jump
	- quit for quitting game
	- Enemies can only be killed by vertically jumping on them

Game Features:
	- There are three different levels of game which tests gamer with different difficulty levels.
	- Score, Coins, Lives and level number are displayed on screen
	- Basic Movements plus gravity like effect for jump
	- There are many types of objects in game:
		1)Clouds
		2)Mountains
		3)Bricks with treasure
		4)Breakable Bricks
		5)Floor
		6)Floor Gaps
		7)Steps
		8)Grass
		9)Flag
		10)Castle

	- Power Ups:
		1)Mario's size increases with mushroom
		2)Mario's number of lives increases

	- Enemies:
		1)Automatically Moving enemies
		2)Boss enemies:
			- Can Fire Bullets
			- Hard to eliminate,recommended to just escape

	- Scenery:
		- First Level scenery is maintained as close to original game as possible to make close enough clone.
		- Background objects stay in background,and they don't disappear even if enemy/player come in front of them
		- Scenery doesn't change abruptly,there's smooth transition from one scene to another.

	- Color:
		- Using colorama,game's color scheme try to follow original mario game

	- Sound:
		- Different sound for jump,attack,death and background music

Code Features:
	- OO Concepts are strictly followed
	- Code follows PEP8 standards