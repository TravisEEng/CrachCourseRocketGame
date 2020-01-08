class GameStats:
	#Track stats for Alien invasion

	def __init__(self,ai_game):
		#Initialize statistics.
		self.settings = ai_game.settings
		self.reset_stats()

		#High score should not reset
		self.high_score = 0

		#Start game in active state
		self.game_active = False

	def reset_stats(self):
		#Initalize statistics that can change during the game.
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

