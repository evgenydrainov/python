class Card:
	def __init__(self, color, value):
		self.color = color
		self.value = value

	def is_special(self):
		return False

	def can_play(self, top_card, color):
		return self.color == color or self.value == top_card.value

	def special_action(self, game):
		pass

	def __str__(self):
		return f"{self.color.name} {self.value}"


class ReverseCard(Card):
	def __init__(self):
		super().__init__(None, -10)

	def is_special(self):
		return True

	def special_action(self, game):
		game.reverse_direction()

	def can_play(self, top_card, color):
		return True

	def __str__(self):
		return "Reverse"


class TakeTwoCard(Card):
	def __init__(self, color):
		super().__init__(color, -11)

	def is_special(self):
		return True

	def special_action(self, game):
		game.force_take_cards = 2
		game.skip_next_turn = True

	def can_play(self, top_card, color):
		return self.color == color or top_card.value == -11

	def __str__(self):
		return f"{self.color.name} Take 2"


class SkipCard(Card):
	def __init__(self, color):
		super().__init__(color, -12)

	def is_special(self):
		return True

	def special_action(self, game):
		game.skip_next_turn = True

	def can_play(self, top_card, color):
		return self.color == color or top_card.value == -12

	def __str__(self):
		return f"{self.color.name} Skip"


class WildCard(Card):
	def __init__(self):
		super().__init__(None, -13)

	def is_special(self):
		return True

	def special_action(self, game):
		game.choose_color()

	def can_play(self, top_card, color):
		return True

	def __str__(self):
		return "Wild Card"


class WildTakeFourCard(Card):
	def __init__(self):
		super().__init__(None, -14)

	def is_special(self):
		return True

	def special_action(self, game):
		game.choose_color()
		game.force_take_cards = 4
		game.skip_next_turn = True

	def can_play(self, top_card, color):
		return True

	def __str__(self):
		return "Wild Card +4"
