class Player:
	def __init__(self):
		self.deck = []
	
	def print_deck(self):
		for i in range(len(self.deck)):
			card = self.deck[i]
			print(f"{i}: {card}")
