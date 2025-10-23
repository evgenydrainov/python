import random
from color import Color
from card import Card, ReverseCard, TakeTwoCard, SkipCard, WildCard, WildTakeFourCard
from player import Player

NUM_DEAL_CARDS = 7

class Game:
	def __init__(self):
		self.deck = []
		self.discard = []
		self.players = []
		self.player_index = 0
		self.play_direction = 1
		self.color = None
		self.playing = True
		self.skip_next_turn = False
		self.force_take_cards = 0

	def initialize_deck(self):
		for color in Color:
			for value in range(2):
				self.deck.append(Card(color, value))
				if value != 0:
					self.deck.append(Card(color, value))

		for color in Color:
			self.deck.append(ReverseCard())
			for i in range(2):
				self.deck.append(TakeTwoCard(color))
				self.deck.append(SkipCard(color))

		for i in range(4):
			self.deck.append(WildCard())
			self.deck.append(WildTakeFourCard())

		random.shuffle(self.deck)

		while True:
			card = self.deck[-1]
			if not card.is_special():
				self.discard.append(card)
				self.deck.pop()
				self.color = self.discard[-1].color
				break
			else:
				random.shuffle(self.deck)

	def deal_cards(self):
		for player in self.players:
			for i in range(NUM_DEAL_CARDS):
				card = self.deck.pop()
				player.deck.append(card)

	def play(self):
		print("Enter num of players: ", end="")
		num_players = int(input())
		print()
		for i in range(num_players):
			player = Player()
			self.players.append(player)

		self.initialize_deck()
		self.deal_cards()
		
		while self.playing:
			self.play_turn()

			player = self.players[self.player_index]
			if len(player.deck) == 0:
				print(f"Player {self.player_index} has Won!")
				print()
				self.playing = False
				break

			self.player_index += self.play_direction
			self.player_index %= len(self.players)

	def play_turn(self):
		if self.force_take_cards > 0:
			self.draw_cards(self.force_take_cards)
			self.force_take_cards = 0

		if self.skip_next_turn:
			print(f"Turn of Player {self.player_index} is skipped")
			print()
			self.skip_next_turn = False
			return

		print(f"Turn of Player: {self.player_index}")
		print(f"Top Card: {self.discard[-1]}")
		print(f"Color: {self.color.name}")
		print(f"Deck has {len(self.deck)} cards")
		print(f"Discard has {len(self.discard)} cards")
		print()

		player = self.players[self.player_index]
		player.print_deck()
		print()

		playable = []
		for i in range(len(player.deck)):
			if self.can_play_card(player.deck[i]):
				playable.append(i)
		
		if len(playable) == 0:
			print("You cannot play any card and have to draw")
			drew = self.draw_cards(1)
			if drew and self.can_play_card(player.deck[-1]):
				print("Taken card can be played")
				print()
				player.print_deck()
				playable.append(len(player.deck) - 1)
			else:
				print("Turn is skipped")
				print()
				return

		while True:
			print("Select card (-1 to draw card): ", end="")
			try:
				card_index = int(input())
				print()
				if card_index == -1:
					self.draw_cards(1)
					print()
					break
				elif card_index in playable:
					self.play_card(card_index)
					break
				else:
					print("Cannot play card")
					print()
			except ValueError:
				print("Cannot play card: Invalid input")
				print()

	def draw_cards(self, count):
		result = False
		
		player = self.players[self.player_index]

		for _ in range(count):
			card = None
			if len(self.deck) > 0:
				card = self.deck.pop()
			elif len(self.discard) > 1:
				card = self.discard.pop(0)

			if card is not None:
				player.deck.append(card)
				print(f"Player {self.player_index} took {card}")
				result = True
			else:
				print("Cannot draw card")
		
		return result

	def play_card(self, card_index):
		player = self.players[self.player_index]

		card = player.deck.pop(card_index)
		self.discard.append(card)
		if card.color is not None:
			self.color = card.color
		
		card.special_action(self)

		print(f"Player {self.player_index} has played {card}")
		print()

	def can_play_card(self, card):
		top_card = self.discard[-1]
		return card.can_play(top_card, self.color)

	def reverse_direction(self):
		self.play_direction = -self.play_direction

	def choose_color(self):
		colors = [color for color in Color]

		for i in range(len(colors)):
			print(f"{i}: {colors[i].name}")

		print("Choose color: ", end="")
		while True:
			try:
				choice = int(input())
				if 0 <= choice < len(colors):
					self.color = colors[choice]
					break
				else:
					print("Invalid index")
			except ValueError:
				print("Invalid input")
