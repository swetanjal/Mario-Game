class Fire:
	def __init__(self, X, Y, speed):
		self.X = X
		self.Y = Y
		self.speed = speed
	def update(self):
		self.X = self.X + self.speed