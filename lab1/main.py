import random
from enum import Enum

class Suit(Enum):
	Hearts   = 0
	Diamonds = 1
	Clubs    = 2
	Spades   = 3

def get_rank_name(rank):
	match rank:
		case 11:
			return "Jack"
		case 12:
			return "Queen"
		case 13:
			return "King"
		case 14:
			return "Ace"
		case _:
			return str(rank)

def get_card_value(card):
	match card.rank:
		case 11 | 12 | 13:
			# Jack, Queen, King
			return 10
		case 14:
			return 1 # TODO
		case _:
			return card.rank

class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	
	def __str__(self):
		return f"{get_rank_name(self.rank)} of {self.suit.name}"

def generate_deck():
	deck = []

	# 11 - Jack
	# 12 - Queen
	# 13 - King
	# 14 - Ace
	ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	for suit in Suit:
		for rank in ranks:
			deck.append(Card(suit, rank))

	random.shuffle(deck)

	return deck

def get_deck_value(deck):
	value = 0
	for card in deck:
		value += get_card_value(card)
	
	return value

def game_loop():
	print("Welcome to Game of 21!")
	print()

	deck = generate_deck()
	player_deck = []
	bot_deck = []
	game_is_over = False
	game_winner = 0
	turn = 0

	while not game_is_over:
		match turn:
			case 0:
				# bot's turn
				
				# bot's turn is always hit because if bot's deck value is
				# over 21 then the game is already over

				card = deck.pop()
				bot_deck.append(card)
				print(f"Bot took card: {card}.")
				print(f"Bot's deck value is now {get_deck_value(bot_deck)}.")
				print()

			case 1:
				# player's turn
				player_choice = 1

				if len(player_deck) >= 2:
					print("1. Hit")
					print("2. Stand")

					got_input = False
					while not got_input:
						try:
							player_choice = int(input())
							got_input = player_choice == 1 or player_choice == 2
						except ValueError:
							got_input = False

						if not got_input:
							print("Invalid input.")
					
				match player_choice:
					case 1:
						# hit
						card = deck.pop()
						player_deck.append(card)
						print(f"Player took card: {card}.")
						print(f"Your deck's value is now {get_deck_value(player_deck)}.")
						print()
					case 2:
						# stand
						print("You decided to stand.")
						print()
				
		# check win condition
		if get_deck_value(player_deck) == 21 or get_deck_value(bot_deck) > 21:
			game_is_over = True
			game_winner = 1
		elif get_deck_value(player_deck) > 21 or get_deck_value(bot_deck) == 21:
			game_is_over = True
			game_winner = 0
		
		# next turn
		turn = 0 if turn == 1 else 1
	
	if game_winner == 1:
		print("You have won!")
	else:
		print("You have lost!")
		
game_loop()
