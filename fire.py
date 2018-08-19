class Fire:
	def __init__(self, X, Y, speed):
		self.X = X
		self.Y = Y
		self.speed = speed
	def update(self, mario, board):
		for i in range(3):
			for j in range(3):
				for k in range(2):
					for l in range(2):
						if mario.X + i == self.X + k and mario.Y + j == self.Y + l:
							board.game_over = 1
							return
		self.X = self.X + self.speed

	def __del__(self):
		pass