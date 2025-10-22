import random
from enum import Enum

class Color(Enum):
	Blue   = 0
	Yellow = 1
	Green  = 2
	Red    = 3

class Card:
	def __init__(self, color, value):
		self.color = color
		self.value = value

class Player:
	def __init__(self):
		pass

class Game:
	def __init__(self):
		self.players = []

	def play(self):
		print("num players: ")
		num_players = int(input())
		for i in range(num_players):
			player = Player()
			self.players.append(player)

game = Game()
game.play()
