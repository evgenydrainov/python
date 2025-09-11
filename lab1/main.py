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
			# Ace
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

def print_card_ascii_art(card):
	ART_W = 19
	ART_H = 9
	art = [[" " for _ in range(ART_W)] for _ in range(ART_H)]

	# fill borders

	# top border
	for x in range(1, ART_W - 1):
		art[0][x] = "_"
	
	# bottom border
	for x in range(1, ART_W - 1):
		art[ART_H - 1][x] = "-"
	
	# left border
	for y in range(1, ART_H - 1):
		art[y][0] = "|"
	
	# right border
	for y in range(1, ART_H - 1):
		art[y][ART_W - 1] = "|"
	
	# fill top left number
	match card.rank:
		case 14:
			art[1][2] = "A"
		case 13:
			art[1][2] = "K"
		case 12:
			art[1][2] = "Q"
		case 11:
			art[1][2] = "J"
		case 10:
			art[1][2] = "1"
			art[1][3] = "0"
		case _:
			art[1][2] = str(card.rank)

	# fill bottom right number
	match card.rank:
		case 2:
			art[ART_H - 2][ART_W - 3] = "5"
		case 3:
			art[ART_H - 2][ART_W - 3] = "E"
		case 4:
			art[ART_H - 2][ART_W - 3] = "b"
		case 5:
			art[ART_H - 2][ART_W - 3] = "2"
		case 6:
			art[ART_H - 2][ART_W - 3] = "9"
		case 7:
			art[ART_H - 2][ART_W - 3] = "L"
		case 8:
			art[ART_H - 2][ART_W - 3] = "8"
		case 9:
			art[ART_H - 2][ART_W - 3] = "6"
		case 10:
			art[ART_H - 2][ART_W - 3] = "l"
			art[ART_H - 2][ART_W - 4] = "0"
		case 11:
			art[ART_H - 2][ART_W - 3] = "P"
		case 12:
			art[ART_H - 2][ART_W - 3] = "Q"
		case 13:
			art[ART_H - 2][ART_W - 3] = "X"
		case 14:
			art[ART_H - 2][ART_W - 3] = "V"

	suit_chars = {
		Suit.Hearts:   "+",
		Suit.Diamonds: "o",
		Suit.Clubs:    "#",
		Suit.Spades:   "*",
	}

	c = suit_chars[card.suit]

	# fill top and bottom card suit chars
	art[2][2] = c
	art[ART_H - 3][ART_W - 3] = c

	# fill center thing

	if card.rank == 2 or card.rank == 3 or card.rank == 10:
		art[2][9] = c
		art[6][9] = c

	if card.rank == 3 or card.rank == 5 or card.rank == 9:
		art[4][9] = c
	
	if card.rank == 4 or card.rank == 5 or card.rank == 6 or card.rank == 7 or card.rank == 8:
		art[2][6] = c
		art[2][12] = c
		art[6][6] = c
		art[6][12] = c
	
	if card.rank == 6 or card.rank == 7 or card.rank == 8:
		art[4][6] = c
		art[4][12] = c
	
	if card.rank == 7 or card.rank == 8:
		art[3][9] = c
	
	if card.rank == 8:
		art[5][9] = c
	
	if card.rank == 9 or card.rank == 10:
		art[1][6] = c
		art[1][12] = c
		art[3][6] = c
		art[3][12] = c
		art[5][6] = c
		art[5][12] = c
		art[7][6] = c
		art[7][12] = c
	
	# special art

	# 9 x 6
	jack_special_art = """
.....###.
......#..
......#..
..#...#..
....#....
........."""

	# 9 x 6
	queen_special_art = """
....#....
.#.....#.
.#.....#.
.#.....#.
....#.#..
........#"""

	# 9 x 6
	king_special_art = """
..#...#..
..#..#...
..#.#....
..#..#...
..#...#..
........."""

	# 9 x 6
	ace_special_art = """
....#....
...#.#...
..#####..
.#.....#.
#.......#
........."""

	special_art = None
	if card.rank == 11:
		special_art = jack_special_art
	elif card.rank == 12:
		special_art = queen_special_art
	elif card.rank == 13:
		special_art = king_special_art
	elif card.rank == 14:
		special_art = ace_special_art

	SPECIAL_ART_W = 9
	SPECIAL_ART_H = 6

	if special_art is not None:
		for y in range(SPECIAL_ART_H):
			for x in range(SPECIAL_ART_W):
				if special_art[x + y * (SPECIAL_ART_W + 1) + 1] != ".":
					art[y + 2][x + 5] = c

	# print the art
	for y in range(ART_H):
		for x in range(ART_W):
			print(art[y][x], end="")
		print()

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
				print_card_ascii_art(card)
				print(f"Bot's deck value is now {get_deck_value(bot_deck)}.")
				print()

			case 1:
				# player's turn
				player_choice = 1

				if len(player_deck) >= 2:
					got_input = False
					while not got_input:
						print("1. Hit")
						print("2. Stand")

						try:
							player_choice = int(input())
							got_input = player_choice == 1 or player_choice == 2
						except ValueError:
							got_input = False

						if not got_input:
							print("Invalid input. Try again.")
							print()
					
				match player_choice:
					case 1:
						# hit
						card = deck.pop()
						player_deck.append(card)
						print(f"Player took card: {card}.")
						print_card_ascii_art(card)
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
