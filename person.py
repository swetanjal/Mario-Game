#Class containing defintion of game characters like Mario, enemies, etc.
class Person:
	#Sets up the Person object
	def __init__(self, X, Y, HEIGHT, WIDTH):
		self.X = X
		self.Y = Y
		self.height = HEIGHT
		self.width = WIDTH
	#Changes the position of Person object
	def update(self, move_x, move_y):
		self.X = self.X + move_x
		self.Y = self.Y + move_y